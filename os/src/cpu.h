/* cpu.h: memory segments (GDT), interrupts (IDT) and the crash screen. */
#ifndef CPU_H
#define CPU_H
#include <stdint.h>

/* what isr_common in cpu.S saved, in the order it sits on the stack */
struct regs {
    uint32_t gs, fs, es, ds;
    uint32_t edi, esi, ebp, esp, ebx, edx, ecx, eax;   /* from pushal */
    uint32_t int_no, err_code;                          /* from our stub */
    uint32_t eip, cs, eflags;                           /* from the CPU */
};

typedef void (*irq_handler_t)(struct regs *r);

void gdt_init(void);
void idt_init(void);
void irq_install(int irq, irq_handler_t handler);
void panic(const char *message);
#endif
