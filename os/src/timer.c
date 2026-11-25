#include "timer.h"
#include "cpu.h"
#include "io.h"

static volatile uint32_t ticks;
static uint32_t frequency = 1;

static void on_tick(struct regs *r) { (void)r; ticks++; }

void timer_init(uint32_t hz) {
    frequency = hz;
    uint32_t divisor = 1193182 / hz;      /* the PIT counts at 1.193182 MHz */
    outb(0x43, 0x36);                     /* channel 0, repeat forever */
    outb(0x40, divisor & 0xFF);
    outb(0x40, (divisor >> 8) & 0xFF);
    irq_install(0, on_tick);              /* the timer is IRQ 0 */
}

uint32_t timer_ticks(void) { return ticks; }
uint32_t timer_hz(void) { return frequency; }
uint32_t uptime_seconds(void) { return ticks / frequency; }

void timer_sleep_ms(uint32_t ms) {
    uint32_t end = ticks + ms * frequency / 1000;
    while ((int32_t)(end - ticks) > 0) cpu_halt();
}
