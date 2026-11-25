/* kernel.c: kernel_main is where our OS starts, called by boot.S. */
#include <stdint.h>
#include "os.h"
#include "io.h"
#include "console.h"
#include "serial.h"
#include "cpu.h"
#include "timer.h"
#include "keyboard.h"
#include "memory.h"
#include "shell.h"

#define MULTIBOOT_MAGIC 0x2BADB002

static void ok(const char *what) {
    console_set_color(LIGHT_GREEN, BLACK);
    kprintf("[ OK ] ");
    console_set_color(LIGHT_GREY, BLACK);
    kprintf("%s\n", what);
}

static void logo(void) {
    console_set_color(LIGHT_CYAN, BLACK);
    kprintf("  __  __        ___  ____  \n");
    kprintf(" |  \\/  |_   _ / _ \\/ ___| \n");
    kprintf(" | |\\/| | | | | | | \\___ \\ \n");
    kprintf(" | |  | | |_| | |_| |___) |\n");
    kprintf(" |_|  |_|\\__, |\\___/|____/ \n");
    kprintf("         |___/   ");
    console_set_color(WHITE, BLACK);
    kprintf("Welcome to %s %s\n\n", OS_NAME, OS_VERSION);
    console_set_color(LIGHT_GREY, BLACK);
}

void kernel_main(uint32_t magic, struct multiboot_info *mbi) {
    serial_init();
    console_init();
    logo();
    if (magic != MULTIBOOT_MAGIC) kprintf("Warning: not started by a multiboot bootloader\n");

    gdt_init();      ok("GDT: memory segments loaded");
    idt_init();      ok("IDT: interrupt handlers installed");
    timer_init(100); ok("Timer: ticking 100 times a second");
    keyboard_init(); ok("Keyboard: ready");
    memory_init(magic == MULTIBOOT_MAGIC ? mbi : 0);
    char line[48];
    ksnprintf(line, sizeof line, "Memory: %u MiB found", pages_total() / 256);
    ok(line);

    interrupts_on(); /* from now on, the timer and keyboard can interrupt us */
    shell_run();
}
