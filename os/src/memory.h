/* memory.h: which parts of RAM are free, in 4 KiB "pages". */
#ifndef MEMORY_H
#define MEMORY_H
#include <stdint.h>
#include <stddef.h>

struct multiboot_info {
    uint32_t flags, mem_lower, mem_upper, boot_device, cmdline, mods_count, mods_addr;
    uint32_t syms[4];
    uint32_t mmap_length, mmap_addr;
} __attribute__((packed));

#define PAGE_SIZE 4096
void memory_init(struct multiboot_info *mbi);
uint32_t page_alloc(void);          /* the address of a free page, or 0 */
void page_free(uint32_t address);
uint32_t pages_total(void);
uint32_t pages_used(void);
void *kmalloc(size_t size);         /* small allocations from a 64 KiB heap */
size_t heap_used(void);
size_t heap_size(void);
#endif
