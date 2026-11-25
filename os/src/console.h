/* console.h: text on the screen. The VGA text screen is 80 x 25 characters;
   each one is 2 bytes in memory at 0xB8000: the character, then its colours. */
#ifndef CONSOLE_H
#define CONSOLE_H
#include <stdint.h>
#include <stdbool.h>

enum color {
    BLACK, BLUE, GREEN, CYAN, RED, MAGENTA, BROWN, LIGHT_GREY,
    DARK_GREY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, PINK, YELLOW, WHITE
};

#define SCREEN_W 80
#define SCREEN_H 25
#define VGA_MEMORY ((volatile uint16_t *)0xB8000)

void console_init(void);
void console_clear(void);
void console_set_color(enum color fg, enum color bg);
void console_putc(char c);
void console_write(const char *s);
void console_cursor(bool visible);

void kprintf(const char *fmt, ...);
int ksnprintf(char *buf, unsigned size, const char *fmt, ...);
#endif
