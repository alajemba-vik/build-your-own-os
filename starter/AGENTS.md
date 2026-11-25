# Instructions for the AI helping me build my operating system

I'm a student building a tiny operating system from scratch, following the aivancity Tech Club
tutorial (https://alajemba-vik.github.io/build-your-own-os/). I may be new to C and to low-level code.
Coding agents (Claude Code, Codex, Cursor, Copilot…) read this file automatically.
If you are a chat AI (ChatGPT, Claude.ai, Gemini…), I pasted it at the start: keep it in mind all the time.

## What this project is
- A **32-bit x86** kernel (i686), written in **C (gnu11)** plus a little **GNU assembler** (`.S` files, AT&T syntax).
- It boots with **Multiboot 1** (header in `src/boot.S`). QEMU loads it directly: `qemu-system-i386 -kernel build/kernel.elf`. No GRUB, no ISO.
- It runs **inside QEMU**, an emulated PC, on my Mac or on Windows (through WSL / Ubuntu). It does not replace macOS or Windows.
- Built with **clang** (`--target=i686-elf`) and **ld.lld**, using the `Makefile`. Commands: `make`, `make run`, `make run-text`, `make run-serial`, `make clean`.
- **Freestanding**: there is no C library. No `printf`, `malloc`, `string.h` from the system, no `#include <stdio.h>`. Only the compiler's own headers are allowed: `stdint.h`, `stddef.h`, `stdbool.h`, `stdarg.h`. Anything else we write ourselves.
- No 64-bit division or modulo (`uint64_t / x`): it needs a helper library we don't have. Use shifts, or 32-bit numbers.
- No floating point (`-mgeneral-regs-only`).
- New `.c` and `.S` files in `src/` are built automatically by the Makefile.

## The plan (one chapter at a time)
1. Boot and print to the screen (done in the starter)
2. A console: scrolling, newlines, colours, `kprintf`, and the serial port (COM1) for debugging
3. GDT and IDT: interrupts, and a red "kernel panic" screen for CPU exceptions
4. The PIC, the PIT timer (100 Hz) and the PS/2 keyboard (IRQ 0 and 1)
5. A shell with commands (help, clear, echo, uptime…)
6. Memory: the multiboot memory map, a bitmap page allocator, a simple `kmalloc`
7. A text-mode desktop with windows (box-drawing characters, double buffering)
8. Make it mine: my own feature, then share it

## How to help me
- **Small steps.** Change only what the current step needs, one feature at a time, so I can test after each one.
- **Explain as you go.** Before the code, say in 2-4 plain sentences what the hardware does and why. Explain every new word once (port, interrupt, scancode…).
- **Show whole files** or clearly marked changes, and tell me which file each part goes in.
- **Tell me how to test it**: the command to run and exactly what I should see.
- **When I paste an error**, explain what it means first, then the fix.
- Keep comments short and useful. Keep names clear.
- Don't add things from later chapters before I ask. Don't switch to 64-bit, GRUB, Rust, or another toolchain.
- If you are not sure about a hardware detail, say so and point me to the OSDev wiki (https://wiki.osdev.org).

## Good to know
- The screen is VGA text mode at `0xB8000`: 80x25 cells, 2 bytes each (character, colour).
- I/O ports: `outb`/`inb` with inline assembly.
- `make run` also connects the serial port to my terminal: anything sent to COM1 (0x3F8) shows there, and what I type there can be read from COM1.
- If QEMU closes or restarts by itself, it is usually a "triple fault" (a crash while handling a crash). `-no-reboot` is set, so QEMU just stops.
