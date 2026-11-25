/* timer.h: the PIT chip interrupts us many times per second, so we can count time. */
#ifndef TIMER_H
#define TIMER_H
#include <stdint.h>
void timer_init(uint32_t hz);
uint32_t timer_ticks(void);
uint32_t timer_hz(void);
uint32_t uptime_seconds(void);
void timer_sleep_ms(uint32_t ms);
#endif
