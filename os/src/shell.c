/* shell.c: read a line, find the command, run it, repeat. */
#include "shell.h"
#include "console.h"
#include "keyboard.h"
#include "timer.h"
#include "memory.h"
#include "string.h"
#include "io.h"
#include "os.h"

#define LINE 128

static void read_line(char *buf, int max) {
    int len = 0;
    for (;;) {
        int c = input_getc();
        if (c == '\n') { console_putc('\n'); buf[len] = 0; return; }
        if (c == '\b') { if (len > 0) { len--; console_putc('\b'); } continue; }
        if (c >= 32 && c < 127 && len < max - 1) { buf[len++] = (char)c; console_putc((char)c); }
    }
}

static void cmd_help(const char *args);

static void cmd_clear(const char *args) { (void)args; console_clear(); }
static void cmd_echo(const char *args) { kprintf("%s\n", args); }

static void cmd_uptime(const char *args) {
    (void)args;
    uint32_t s = uptime_seconds();
    kprintf("Up for %02u:%02u:%02u (%u timer ticks)\n", s / 3600, (s / 60) % 60, s % 60, timer_ticks());
}

static void cmd_mem(const char *args) {
    (void)args;
    uint32_t total = pages_total(), used = pages_used();
    kprintf("Memory: %u MiB usable, %u pages of 4 KiB\n", total / 256, total);
    kprintf("Used:   %u pages   Free: %u pages\n", used, total - used);
    kprintf("Heap:   %u of %u bytes used\n", (uint32_t)heap_used(), (uint32_t)heap_size());
}

static void cmd_alloc(const char *args) {
    (void)args;
    uint32_t page = page_alloc();
    if (page) kprintf("Got a free page at %p\n", page);
    else kprintf("Out of memory\n");
}

static void cmd_about(const char *args) {
    (void)args;
    kprintf("%s %s: a tiny operating system for 32-bit x86 PCs.\n", OS_NAME, OS_VERSION);
    kprintf("Written in C, from scratch, with no help from Windows, macOS or Linux.\n");
    kprintf("Running for %u seconds on %u MiB of memory.\n", uptime_seconds(), pages_total() / 256);
}

static const struct { const char *name; enum color fg; } colors[] = {
    { "white", WHITE }, { "grey", LIGHT_GREY }, { "green", LIGHT_GREEN }, { "cyan", LIGHT_CYAN },
    { "blue", LIGHT_BLUE }, { "yellow", YELLOW }, { "pink", PINK }, { "red", LIGHT_RED },
};

static void cmd_color(const char *args) {
    for (unsigned i = 0; i < sizeof colors / sizeof colors[0]; i++)
        if (strcmp(args, colors[i].name) == 0) { console_set_color(colors[i].fg, BLACK); kprintf("Colour changed.\n"); return; }
    kprintf("Try one of:");
    for (unsigned i = 0; i < sizeof colors / sizeof colors[0]; i++) kprintf(" %s", colors[i].name);
    kprintf("\n");
}

static void cmd_desktop(const char *args) { (void)args; desktop_run(); }

static void cmd_crash(const char *args) {
    (void)args;
    kprintf("Running an instruction that does not exist...\n");
    __asm__ volatile ("ud2");                  /* "invalid opcode": shows the panic screen */
}

static void cmd_reboot(const char *args) {
    (void)args;
    kprintf("Restarting...\n");
    while (inb(0x64) & 2) { }
    outb(0x64, 0xFE);                          /* ask the keyboard chip to reset the CPU */
    for (;;) cpu_halt();
}

static void cmd_shutdown(const char *args) {
    (void)args;
    kprintf("Shutting down. Bye!\n");
    outw(0x604, 0x2000);                       /* QEMU */
    outw(0xB004, 0x2000);                      /* older QEMU and Bochs */
    outw(0x4004, 0x3400);                      /* VirtualBox */
    outb(0xF4, 0x00);                          /* QEMU's test device, used by the automatic test */
    interrupts_off();
    for (;;) cpu_halt();
}

static const struct command {
    const char *name, *help;
    void (*run)(const char *args);
} commands[] = {
    { "help",     "list the commands",                  cmd_help },
    { "clear",    "clear the screen",                   cmd_clear },
    { "echo",     "print some text: echo hello",        cmd_echo },
    { "about",    "about this OS",                      cmd_about },
    { "uptime",   "time since boot",                    cmd_uptime },
    { "mem",      "memory use",                         cmd_mem },
    { "alloc",    "take one free page of memory",       cmd_alloc },
    { "color",    "change the text colour: color cyan", cmd_color },
    { "desktop",  "open the desktop",                   cmd_desktop },
    { "crash",    "see what a crash looks like",        cmd_crash },
    { "reboot",   "restart the computer",               cmd_reboot },
    { "shutdown", "turn the computer off",              cmd_shutdown },
};
#define COMMANDS (sizeof commands / sizeof commands[0])

static void cmd_help(const char *args) {
    (void)args;
    kprintf("Commands:\n");
    for (unsigned i = 0; i < COMMANDS; i++) kprintf("  %-10s %s\n", commands[i].name, commands[i].help);
}

static void run(char *line) {
    while (*line == ' ') line++;
    if (!*line) return;
    char *args = line;
    while (*args && *args != ' ') args++;
    if (*args) *args++ = 0;                    /* split "echo hi" into "echo" and "hi" */
    while (*args == ' ') args++;
    for (unsigned i = 0; i < COMMANDS; i++)
        if (strcmp(line, commands[i].name) == 0) { commands[i].run(args); return; }
    kprintf("Unknown command: %s (type help)\n", line);
}

void shell_run(void) {
    char line[LINE];
    kprintf("\nType help to see what you can do.\n");
    for (;;) {
        console_set_color(LIGHT_CYAN, BLACK);
        kprintf("%s> ", OS_NAME);
        console_set_color(LIGHT_GREY, BLACK);
        read_line(line, LINE);
        run(line);
    }
}
