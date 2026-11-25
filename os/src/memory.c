/* memory.c: a "bitmap" page allocator. One bit per 4 KiB page: 1 = used, 0 = free.
   The bootloader tells us which areas of RAM exist; everything else stays marked used. */
#include "memory.h"
#include "string.h"
#include <stdbool.h>

struct mmap_entry {
    uint32_t size;
    uint64_t addr, len;
    uint32_t type;                 /* 1 = RAM we may use */
} __attribute__((packed));

#define MAX_PAGES (512u * 1024 * 1024 / PAGE_SIZE)     /* we handle up to 512 MiB */
static uint32_t bitmap[MAX_PAGES / 32];
static uint32_t total, used;
extern char kernel_end[];                              /* set by linker.ld */

static bool is_used(uint32_t p) { return bitmap[p / 32] & (1u << (p % 32)); }
static void mark_used(uint32_t p) { bitmap[p / 32] |= 1u << (p % 32); }
static void mark_free(uint32_t p) { bitmap[p / 32] &= ~(1u << (p % 32)); }

static void free_range(uint64_t start, uint64_t length) {
    uint64_t first = (start + PAGE_SIZE - 1) >> 12, last = (start + length) >> 12;
    for (uint64_t p = first; p < last && p < MAX_PAGES; p++)
        if (is_used((uint32_t)p)) { mark_free((uint32_t)p); total++; }
}

void memory_init(struct multiboot_info *mbi) {
    memset(bitmap, 0xFF, sizeof bitmap);                      /* start with everything used */
    if (mbi && (mbi->flags & (1 << 6))) {                     /* we got a memory map */
        uint32_t p = mbi->mmap_addr, end = p + mbi->mmap_length;
        while (p < end) {
            struct mmap_entry *e = (struct mmap_entry *)p;
            if (e->type == 1) free_range(e->addr, e->len);
            p += e->size + 4;
        }
    } else if (mbi && (mbi->flags & 1)) {                     /* only the total size */
        free_range(0x100000, (uint64_t)mbi->mem_upper << 10);
    }
    uint32_t reserved = ((uint32_t)kernel_end + PAGE_SIZE - 1) >> 12;
    for (uint32_t p = 0; p < reserved; p++)                   /* the first 1 MiB and our kernel */
        if (!is_used(p)) { mark_used(p); used++; }
}

uint32_t page_alloc(void) {
    for (uint32_t i = 0; i < MAX_PAGES / 32; i++) {
        if (bitmap[i] == 0xFFFFFFFF) continue;                /* 32 used pages: skip fast */
        for (uint32_t b = 0; b < 32; b++) {
            uint32_t p = i * 32 + b;
            if (!is_used(p)) { mark_used(p); used++; return p * PAGE_SIZE; }
        }
    }
    return 0;                                                 /* out of memory */
}

void page_free(uint32_t address) {
    uint32_t p = address / PAGE_SIZE;
    if (p < MAX_PAGES && is_used(p)) { mark_free(p); used--; }
}

uint32_t pages_total(void) { return total; }
uint32_t pages_used(void) { return used; }

/* the simplest heap: hand out the next free bytes, never take them back */
static uint8_t heap[64 * 1024] __attribute__((aligned(16)));
static size_t heap_top;

void *kmalloc(size_t size) {
    size = (size + 15) & ~(size_t)15;
    if (heap_top + size > sizeof heap) return 0;
    void *p = heap + heap_top;
    heap_top += size;
    return p;
}
size_t heap_used(void) { return heap_top; }
size_t heap_size(void) { return sizeof heap; }
