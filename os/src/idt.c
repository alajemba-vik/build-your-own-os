/* idt.c: the Interrupt Descriptor Table tells the CPU which code to run for each of the
   256 interrupts. 0-31 are CPU errors (exceptions); we move the 16 hardware IRQs to 32-47. */
#include "cpu.h"
#include "io.h"

struct idt_entry {
    uint16_t base_low, selector;
    uint8_t zero, flags;
    uint16_t base_high;
} __attribute__((packed));

struct idt_ptr { uint16_t limit; uint32_t base; } __attribute__((packed));

static struct idt_entry idt[256];
static struct idt_ptr ip;
static irq_handler_t handlers[16];
extern uint32_t isr_stub_table[48];
extern void idt_load(struct idt_ptr *p);
void panic_exception(struct regs *r);

#define PIC1 0x20   /* the main interrupt controller (IRQ 0-7) */
#define PIC2 0xA0   /* the second one (IRQ 8-15), chained to IRQ 2 */

static void pic_remap(void) {
    outb(PIC1, 0x11); io_wait(); outb(PIC2, 0x11); io_wait();         /* start setup */
    outb(PIC1 + 1, 32); io_wait(); outb(PIC2 + 1, 40); io_wait();     /* IRQ 0-7 -> 32-39, 8-15 -> 40-47 */
    outb(PIC1 + 1, 4); io_wait(); outb(PIC2 + 1, 2); io_wait();       /* how the two are chained */
    outb(PIC1 + 1, 1); io_wait(); outb(PIC2 + 1, 1); io_wait();       /* 8086 mode */
    outb(PIC1 + 1, 0xFB);                                             /* mute all IRQs but the chain (2) */
    outb(PIC2 + 1, 0xFF);
}

void irq_install(int irq, irq_handler_t handler) {
    handlers[irq] = handler;
    uint16_t port = irq < 8 ? PIC1 + 1 : PIC2 + 1;
    outb(port, inb(port) & ~(1 << (irq & 7)));                        /* unmute this IRQ */
}

void idt_init(void) {
    for (int i = 0; i < 48; i++) {
        uint32_t base = isr_stub_table[i];
        idt[i].base_low = base & 0xFFFF;
        idt[i].base_high = base >> 16;
        idt[i].selector = 0x08;      /* run it in our code segment */
        idt[i].zero = 0;
        idt[i].flags = 0x8E;         /* present, kernel only, interrupt gate */
    }
    ip.limit = sizeof(idt) - 1;
    ip.base = (uint32_t)&idt;
    pic_remap();
    idt_load(&ip);
}

/* called from isr_common in cpu.S for every interrupt */
void isr_handler(struct regs *r) {
    if (r->int_no < 32) { panic_exception(r); return; }
    int irq = (int)r->int_no - 32;
    if (irq == 7 || irq == 15) {                       /* "spurious" IRQs: check they are real */
        uint16_t pic = irq == 7 ? PIC1 : PIC2;
        outb(pic, 0x0B);
        if (!(inb(pic) & 0x80)) { if (irq == 15) outb(PIC1, 0x20); return; }
    }
    if (handlers[irq]) handlers[irq](r);
    if (irq >= 8) outb(PIC2, 0x20);                    /* "End Of Interrupt": ready for the next one */
    outb(PIC1, 0x20);
}
