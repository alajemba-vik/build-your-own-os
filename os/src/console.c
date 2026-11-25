#include "console.h"
#include "serial.h"
#include "io.h"

static int row, col;
static uint8_t color = LIGHT_GREY | (BLACK << 4);

static inline uint16_t cell(char c, uint8_t attr) { return (uint8_t)c | ((uint16_t)attr << 8); }

static void move_cursor(void) {                 /* the blinking cursor is moved through ports 0x3D4/0x3D5 */
    uint16_t pos = (uint16_t)(row * SCREEN_W + col);
    outb(0x3D4, 0x0F); outb(0x3D5, pos & 0xFF);
    outb(0x3D4, 0x0E); outb(0x3D5, pos >> 8);
}

void console_cursor(bool visible) {
    outb(0x3D4, 0x0A);
    outb(0x3D5, visible ? 14 : 0x20);           /* 0x20 = cursor off */
    if (visible) { outb(0x3D4, 0x0B); outb(0x3D5, 15); }
}

void console_set_color(enum color fg, enum color bg) { color = (uint8_t)(fg | (bg << 4)); }

void console_clear(void) {
    for (int i = 0; i < SCREEN_W * SCREEN_H; i++) VGA_MEMORY[i] = cell(' ', color);
    row = col = 0;
    move_cursor();
}

void console_init(void) { console_cursor(true); console_clear(); }

static void scroll(void) {                      /* move every line up by one, clear the last one */
    for (int i = 0; i < SCREEN_W * (SCREEN_H - 1); i++) VGA_MEMORY[i] = VGA_MEMORY[i + SCREEN_W];
    for (int x = 0; x < SCREEN_W; x++) VGA_MEMORY[(SCREEN_H - 1) * SCREEN_W + x] = cell(' ', color);
    row = SCREEN_H - 1;
}

void console_putc(char c) {
    serial_putc(c);
    if (c == '\n') { col = 0; row++; }
    else if (c == '\r') { col = 0; }
    else if (c == '\b') { if (col > 0) { col--; VGA_MEMORY[row * SCREEN_W + col] = cell(' ', color); } }
    else if (c == '\t') { col = (col + 4) & ~3; }
    else { VGA_MEMORY[row * SCREEN_W + col] = cell(c, color); col++; }
    if (col >= SCREEN_W) { col = 0; row++; }
    if (row >= SCREEN_H) scroll();
    move_cursor();
}

void console_write(const char *s) { while (*s) console_putc(*s++); }
