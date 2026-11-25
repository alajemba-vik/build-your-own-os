#include "serial.h"
#include "io.h"
#include <stdbool.h>

#define COM1 0x3F8

void serial_init(void) {
    outb(COM1 + 1, 0x00);   /* no serial interrupts: we check it ourselves */
    outb(COM1 + 3, 0x80);   /* next two bytes set the speed */
    outb(COM1 + 0, 0x03);   /* 38400 baud */
    outb(COM1 + 1, 0x00);
    outb(COM1 + 3, 0x03);   /* 8 bits, no parity, one stop bit */
    outb(COM1 + 2, 0xC7);   /* turn on the FIFO buffer */
    outb(COM1 + 4, 0x0B);
}

static void raw_put(char c) {
    while ((inb(COM1 + 5) & 0x20) == 0) { }   /* wait until the port can take a byte */
    outb(COM1, (uint8_t)c);
}

void serial_putc(char c) {
    if (c == '\n') raw_put('\r');
    if (c == '\b') { raw_put('\b'); raw_put(' '); }   /* erase the character in the terminal */
    raw_put(c);
}

int serial_getc(void) {
    static bool last_was_cr = false;
    if ((inb(COM1 + 5) & 1) == 0) return -1;
    uint8_t c = inb(COM1);
    if (c == '\n' && last_was_cr) { last_was_cr = false; return -1; }   /* "\r\n" is one Enter */
    last_was_cr = (c == '\r');
    if (c == '\r') return '\n';
    if (c == 0x7F) return '\b';                                         /* terminals send DEL for Backspace */
    return c;
}
