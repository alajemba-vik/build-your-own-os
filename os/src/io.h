/* io.h: tiny helpers to talk to hardware through "I/O ports" and control the CPU. */
#ifndef IO_H
#define IO_H
#include <stdint.h>

static inline void outb(uint16_t port, uint8_t value) { __asm__ volatile ("outb %0, %1" : : "a"(value), "Nd"(port)); }
static inline void outw(uint16_t port, uint16_t value) { __asm__ volatile ("outw %0, %1" : : "a"(value), "Nd"(port)); }
static inline uint8_t inb(uint16_t port) { uint8_t v; __asm__ volatile ("inb %1, %0" : "=a"(v) : "Nd"(port)); return v; }
static inline void io_wait(void) { outb(0x80, 0); }           /* a tiny pause: port 0x80 is unused */
static inline void cpu_halt(void) { __asm__ volatile ("hlt"); } /* sleep until the next interrupt */
static inline void interrupts_on(void) { __asm__ volatile ("sti"); }
static inline void interrupts_off(void) { __asm__ volatile ("cli"); }

#endif
