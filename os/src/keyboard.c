/* keyboard.c: every key press sends a "scancode" on IRQ 1. We turn it into a character
   and keep it in a small queue until someone reads it. The table is for a US (QWERTY) layout. */
#include "keyboard.h"
#include "cpu.h"
#include "io.h"
#include "serial.h"
#include <stdbool.h>
#include <stdint.h>

static const char normal[58] = {
    0, 27, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '\b',
    '\t', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\n',
    0, 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', '`',
    0, '\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 0,
    '*', 0, ' ',
};
static const char shifted[58] = {
    0, 27, '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '\b',
    '\t', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '\n',
    0, 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', '~',
    0, '|', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', 0,
    '*', 0, ' ',
};

#define QUEUE 64
static volatile uint8_t queue[QUEUE];
static volatile unsigned head, tail, presses;
static bool shift, caps, extended;

static void push(uint8_t c) {
    unsigned next = (head + 1) % QUEUE;
    if (next != tail) { queue[head] = c; head = next; }   /* if the queue is full, drop the key */
    presses++;
}

static void on_key(struct regs *r) {
    (void)r;
    uint8_t sc = inb(0x60);
    if (sc == 0xE0) { extended = true; return; }          /* arrow keys come in two parts */
    if (extended) {
        extended = false;
        if (sc == 0x48) push(KEY_UP);
        else if (sc == 0x50) push(KEY_DOWN);
        else if (sc == 0x4B) push(KEY_LEFT);
        else if (sc == 0x4D) push(KEY_RIGHT);
        return;
    }
    if (sc & 0x80) {                                      /* a key was released */
        sc &= 0x7F;
        if (sc == 0x2A || sc == 0x36) shift = false;
        return;
    }
    if (sc == 0x2A || sc == 0x36) { shift = true; return; }
    if (sc == 0x3A) { caps = !caps; return; }
    if (sc >= sizeof normal) return;
    char c = shift ? shifted[sc] : normal[sc];
    if (caps && c >= 'a' && c <= 'z') c -= 32;
    else if (caps && c >= 'A' && c <= 'Z') c += 32;
    if (c) push((uint8_t)c);
}

void keyboard_init(void) {
    while (inb(0x64) & 1) inb(0x60);                      /* throw away anything already waiting */
    irq_install(1, on_key);                               /* the keyboard is IRQ 1 */
}

unsigned keyboard_presses(void) { return presses; }

int input_poll(void) {
    if (head != tail) {
        uint8_t c = queue[tail];
        tail = (tail + 1) % QUEUE;
        return c;
    }
    return serial_getc();                                 /* also accept typing in the terminal */
}

int input_getc(void) {
    for (;;) {
        int c = input_poll();
        if (c >= 0) return c;
        cpu_halt();                                       /* sleep until the next interrupt */
    }
}
