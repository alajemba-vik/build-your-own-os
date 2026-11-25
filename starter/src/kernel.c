/* kernel.c: your operating system starts here.
   boot.S sets up a stack and calls kernel_main. There is no Windows, no macOS, no Linux
   and no C library under us: just the CPU, the memory and the hardware. */
#include <stdint.h>

/* The screen in text mode: 80 columns x 25 rows. Each character is 2 bytes in memory,
   starting at address 0xB8000: first the letter, then its colour (background << 4 | text). */
#define VGA_WIDTH 80
#define VGA_HEIGHT 25
static volatile uint16_t *const vga = (volatile uint16_t *)0xB8000;

static void print_at(int x, int y, const char *text, uint8_t color) {
    for (int i = 0; text[i]; i++)
        vga[y * VGA_WIDTH + x + i] = (uint16_t)(uint8_t)text[i] | ((uint16_t)color << 8);
}

void kernel_main(uint32_t magic, uint32_t multiboot_info) {
    (void)magic;            /* 0x2BADB002 if a multiboot bootloader started us */
    (void)multiboot_info;   /* where the bootloader left information for us (chapter 6) */

    for (int i = 0; i < VGA_WIDTH * VGA_HEIGHT; i++)
        vga[i] = ' ' | (0x07 << 8);                         /* clear the screen: grey on black */

    print_at(2, 1, "Hello from my own operating system!", 0x0B);   /* light cyan */
    print_at(2, 3, "No Windows. No macOS. Just my code and the CPU.", 0x07);
    print_at(2, 5, "Next: chapter 2, a real console with scrolling and printf.", 0x0A);

    for (;;) __asm__ volatile ("hlt");                      /* nothing else to do yet: sleep */
}
