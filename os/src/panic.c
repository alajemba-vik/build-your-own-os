/* panic.c: when something goes very wrong, stop everything and show what happened. */
#include "cpu.h"
#include "console.h"
#include "io.h"

static const char *names[32] = {
    "Division by zero", "Debug", "Non-maskable interrupt", "Breakpoint", "Overflow",
    "Bound range exceeded", "Invalid opcode", "Device not available", "Double fault",
    "Coprocessor segment overrun", "Invalid TSS", "Segment not present", "Stack-segment fault",
    "General protection fault", "Page fault", "Reserved", "x87 floating-point error",
    "Alignment check", "Machine check", "SIMD floating-point error", "Virtualization error",
    "Control protection error", "Reserved", "Reserved", "Reserved", "Reserved", "Reserved",
    "Reserved", "Hypervisor injection", "VMM communication", "Security exception", "Reserved",
};

static void stop(void) {
    kprintf("\nThe system is stopped. Close QEMU to start again.\n");
    for (;;) { interrupts_off(); cpu_halt(); }
}

static void red_screen(const char *title) {
    interrupts_off();
    console_set_color(WHITE, RED);
    console_clear();
    kprintf("\n  KERNEL PANIC\n\n  %s\n\n", title);
}

void panic(const char *message) {
    red_screen(message);
    stop();
}

void panic_exception(struct regs *r) {
    red_screen(names[r->int_no]);
    kprintf("  exception %u   error code %x\n", r->int_no, r->err_code);
    kprintf("  eip %p   (the instruction that failed)\n\n", r->eip);
    kprintf("  eax %p  ebx %p  ecx %p  edx %p\n", r->eax, r->ebx, r->ecx, r->edx);
    kprintf("  esi %p  edi %p  ebp %p  esp %p\n", r->esi, r->edi, r->ebp, r->esp);
    kprintf("\n  Tip: ask your AI what \"%s\" means and which line of code is at eip.\n", names[r->int_no]);
    stop();
}
