/* gdt.c: the Global Descriptor Table. Old x86 chips split memory into "segments".
   We make two segments (code and data) that both cover all 4 GiB, so we can forget about them. */
#include "cpu.h"

struct gdt_entry {
    uint16_t limit_low, base_low;
    uint8_t base_mid, access, granularity, base_high;
} __attribute__((packed));

struct gdt_ptr { uint16_t limit; uint32_t base; } __attribute__((packed));

static struct gdt_entry gdt[3];
static struct gdt_ptr gp;
extern void gdt_flush(struct gdt_ptr *p);

static void set_entry(int i, uint32_t base, uint32_t limit, uint8_t access, uint8_t gran) {
    gdt[i].base_low = base & 0xFFFF;
    gdt[i].base_mid = (base >> 16) & 0xFF;
    gdt[i].base_high = (base >> 24) & 0xFF;
    gdt[i].limit_low = limit & 0xFFFF;
    gdt[i].granularity = ((limit >> 16) & 0x0F) | (gran & 0xF0);
    gdt[i].access = access;
}

void gdt_init(void) {
    set_entry(0, 0, 0, 0, 0);                  /* entry 0 must be empty */
    set_entry(1, 0, 0xFFFFFFFF, 0x9A, 0xCF);   /* 0x08: kernel code, readable */
    set_entry(2, 0, 0xFFFFFFFF, 0x92, 0xCF);   /* 0x10: kernel data, writable */
    gp.limit = sizeof(gdt) - 1;
    gp.base = (uint32_t)&gdt;
    gdt_flush(&gp);
}
