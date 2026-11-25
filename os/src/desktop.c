/* desktop.c: a desktop with windows, drawn with text characters (the VGA font has
   box-drawing characters). We draw into a copy of the screen first, then copy it in
   one go, so nothing flickers. */
#include "shell.h"
#include "console.h"
#include "keyboard.h"
#include "timer.h"
#include "memory.h"
#include "string.h"
#include "io.h"
#include "os.h"
#include <stdbool.h>

static uint16_t frame[SCREEN_W * SCREEN_H];
static uint16_t saved[SCREEN_W * SCREEN_H];

struct window { int x, y, w, h; const char *title; int app; };
static struct window windows[2] = {
    { 4, 3, 36, 12, "Welcome", 0 },
    { 44, 12, 31, 9, "System", 1 },
};
static int focused = 0;

static void put(int x, int y, unsigned char ch, uint8_t attr) {
    if (x >= 0 && x < SCREEN_W && y >= 0 && y < SCREEN_H) frame[y * SCREEN_W + x] = ch | (attr << 8);
}
static void text(int x, int y, const char *s, uint8_t attr) { while (*s) put(x++, y, (unsigned char)*s++, attr); }
static void fill(int x, int y, int w, int h, unsigned char ch, uint8_t attr) {
    for (int j = 0; j < h; j++) for (int i = 0; i < w; i++) put(x + i, y + j, ch, attr);
}

static void draw_window(struct window *win, bool active) {
    const uint8_t body = 0x70;                                  /* black on light grey */
    fill(win->x + 1, win->y + win->h, win->w, 1, ' ', 0x00);    /* shadow */
    fill(win->x + win->w, win->y + 1, 1, win->h, ' ', 0x00);
    fill(win->x, win->y, win->w, win->h, ' ', body);
    /* double lines for the active window, single lines for the other */
    unsigned char tl = active ? 0xC9 : 0xDA, tr = active ? 0xBB : 0xBF, bl = active ? 0xC8 : 0xC0,
                  br = active ? 0xBC : 0xD9, hz = active ? 0xCD : 0xC4, vt = active ? 0xBA : 0xB3;
    for (int i = 1; i < win->w - 1; i++) { put(win->x + i, win->y, hz, body); put(win->x + i, win->y + win->h - 1, hz, body); }
    for (int j = 1; j < win->h - 1; j++) { put(win->x, win->y + j, vt, body); put(win->x + win->w - 1, win->y + j, vt, body); }
    put(win->x, win->y, tl, body); put(win->x + win->w - 1, win->y, tr, body);
    put(win->x, win->y + win->h - 1, bl, body); put(win->x + win->w - 1, win->y + win->h - 1, br, body);
    uint8_t title = active ? 0x30 : 0x78;                       /* black on cyan / grey on grey */
    int len = (int)strlen(win->title) + 2;
    put(win->x + (win->w - len) / 2 - 1, win->y, ' ', title);
    text(win->x + (win->w - len) / 2, win->y, win->title, title);
    put(win->x + (win->w - len) / 2 + len - 2, win->y, ' ', title);

    int x = win->x + 2, y = win->y + 2;
    char line[40];
    if (win->app == 0) {
        text(x, y++, "Hello! This desktop runs on", body);
        ksnprintf(line, sizeof line, "%s %s, an OS you built", OS_NAME, OS_VERSION);
        text(x, y++, line, body);
        text(x, y++, "yourself, from the first byte.", body);
        y++;
        text(x, y++, "Ideas for your next step:", body);
        text(x, y++, "\x07 a clock or a calculator app", body);
        text(x, y++, "\x07 a game (snake fits nicely)", body);
        text(x, y++, "\x07 your own colours and logo", body);
    } else {
        uint32_t s = uptime_seconds();
        ksnprintf(line, sizeof line, "Uptime    %02u:%02u:%02u", s / 3600, (s / 60) % 60, s % 60);
        text(x, y++, line, body);
        ksnprintf(line, sizeof line, "Memory    %u MiB", pages_total() / 256);
        text(x, y++, line, body);
        ksnprintf(line, sizeof line, "Free      %u pages", pages_total() - pages_used());
        text(x, y++, line, body);
        ksnprintf(line, sizeof line, "Keys      %u pressed", keyboard_presses());
        text(x, y++, line, body);
        static const char spin[4] = { '|', '/', '-', '\\' };
        ksnprintf(line, sizeof line, "Working   %c", spin[(timer_ticks() / 10) % 4]);
        text(x, y++, line, body);
    }
}

static void draw(void) {
    fill(0, 0, SCREEN_W, SCREEN_H, 0xB0, 0x13);                 /* textured blue background */
    fill(0, 0, SCREEN_W, 1, ' ', 0x70);                         /* top bar */
    char line[40];
    ksnprintf(line, sizeof line, " %s Desktop", OS_NAME);
    text(0, 0, line, 0x70);
    uint32_t s = uptime_seconds();
    ksnprintf(line, sizeof line, "up %02u:%02u:%02u ", s / 3600, (s / 60) % 60, s % 60);
    text(SCREEN_W - (int)strlen(line), 0, line, 0x70);
    fill(0, SCREEN_H - 1, SCREEN_W, 1, ' ', 0x70);              /* bottom bar */
    text(1, SCREEN_H - 1, "Tab: next window   Arrows or WASD: move it   Esc: back to the shell", 0x70);
    for (int i = 0; i < 2; i++) if (i != focused) draw_window(&windows[i], false);
    draw_window(&windows[focused], true);                       /* the active window goes on top */
    memcpy((void *)VGA_MEMORY, frame, sizeof frame);
}

void desktop_run(void) {
    memcpy(saved, (const void *)VGA_MEMORY, sizeof saved);
    console_cursor(false);
    uint32_t last = 0;
    bool dirty = true;
    for (;;) {
        int c = input_poll();
        if (c == KEY_ESC) break;
        struct window *w = &windows[focused];
        if (c == '\t') focused = (focused + 1) % 2;
        else if (c == KEY_LEFT || c == 'a') w->x--;
        else if (c == KEY_RIGHT || c == 'd') w->x++;
        else if (c == KEY_UP || c == 'w') w->y--;
        else if (c == KEY_DOWN || c == 's') w->y++;
        if (w->x < 0) w->x = 0;
        if (w->x > SCREEN_W - w->w - 1) w->x = SCREEN_W - w->w - 1;
        if (w->y < 1) w->y = 1;
        if (w->y > SCREEN_H - w->h - 2) w->y = SCREEN_H - w->h - 2;
        if (c >= 0) dirty = true;
        if (dirty || timer_ticks() - last >= timer_hz() / 4) {  /* redraw 4 times a second for the clock */
            draw();
            last = timer_ticks();
            dirty = false;
        } else {
            cpu_halt();
        }
    }
    memcpy((void *)VGA_MEMORY, saved, sizeof saved);
    console_cursor(true);
}
