/* printf.c: kprintf("%s has %d pages\n", name, n). Supports %s %c %d %u %x %p %%,
   a width (%5d), zero padding (%02d) and left alignment (%-10s). */
#include "console.h"
#include <stdarg.h>
#include <stdint.h>
#include <stdbool.h>

typedef void (*out_fn)(char c, void *ctx);

static void pad(out_fn out, void *ctx, int n, char c) { while (n-- > 0) out(c, ctx); }

static void format(out_fn out, void *ctx, const char *fmt, va_list ap) {
    for (; *fmt; fmt++) {
        if (*fmt != '%') { out(*fmt, ctx); continue; }
        fmt++;
        bool left = false, zero = false;
        int width = 0;
        if (*fmt == '-') { left = true; fmt++; }
        if (*fmt == '0') { zero = true; fmt++; }
        while (*fmt >= '0' && *fmt <= '9') width = width * 10 + (*fmt++ - '0');

        char num[16];
        int len = 0;
        bool neg = false;
        const char *str = 0;
        switch (*fmt) {
        case 's': str = va_arg(ap, const char *); if (!str) str = "(null)"; break;
        case 'c': num[0] = (char)va_arg(ap, int); num[1] = 0; str = num; break;
        case 'd': case 'i': case 'u': case 'x': case 'p': {
            uint32_t v;
            unsigned base = (*fmt == 'x' || *fmt == 'p') ? 16 : 10;
            if (*fmt == 'd' || *fmt == 'i') { int32_t s = va_arg(ap, int32_t); neg = s < 0; v = neg ? -(uint32_t)s : (uint32_t)s; }
            else v = va_arg(ap, uint32_t);
            if (*fmt == 'p') { out('0', ctx); out('x', ctx); zero = true; width = 8; }
            do { num[len++] = "0123456789abcdef"[v % base]; v /= base; } while (v);
            int total = len + neg;
            if (neg && zero) out('-', ctx);
            if (!left) pad(out, ctx, width - total, zero ? '0' : ' ');
            if (neg && !zero) out('-', ctx);
            while (len) out(num[--len], ctx);
            if (left) pad(out, ctx, width - total, ' ');
            continue;
        }
        case '%': out('%', ctx); continue;
        case 0: return;
        default: out('%', ctx); out(*fmt, ctx); continue;
        }
        int n = 0;
        while (str[n]) n++;
        if (!left) pad(out, ctx, width - n, ' ');
        for (int i = 0; i < n; i++) out(str[i], ctx);
        if (left) pad(out, ctx, width - n, ' ');
    }
}

static void to_console(char c, void *ctx) { (void)ctx; console_putc(c); }

void kprintf(const char *fmt, ...) {
    va_list ap;
    va_start(ap, fmt);
    format(to_console, 0, fmt, ap);
    va_end(ap);
}

struct buf { char *p; unsigned size, used; };
static void to_buf(char c, void *ctx) {
    struct buf *b = ctx;
    if (b->used + 1 < b->size) b->p[b->used] = c;
    b->used++;
}

int ksnprintf(char *p, unsigned size, const char *fmt, ...) {
    struct buf b = { p, size, 0 };
    va_list ap;
    va_start(ap, fmt);
    format(to_buf, &b, fmt, ap);
    va_end(ap);
    if (size) p[b.used < size ? b.used : size - 1] = 0;
    return (int)b.used;
}
