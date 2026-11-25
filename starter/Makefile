# Build and run the OS.
#   make              build build/kernel.elf
#   make run          start it in QEMU (a window, plus the serial output in this terminal)
#   make run-text     show the screen inside this terminal (no window needed)
#   make run-serial   serial port only, no screen (the desktop needs a screen)
#   make clean        delete the build folder

# Find clang and ld.lld: Homebrew on macOS, or the ones on your PATH (Ubuntu / WSL).
BREW := $(shell command -v brew 2>/dev/null)
ifneq ($(BREW),)
  LLVM_DIR := $(shell brew --prefix llvm 2>/dev/null)
  LLD_DIR  := $(shell brew --prefix lld 2>/dev/null)
endif
CLANG := $(firstword $(wildcard $(LLVM_DIR)/bin/clang) clang)
LLD   := $(firstword $(wildcard $(LLD_DIR)/bin/ld.lld $(LLVM_DIR)/bin/ld.lld) ld.lld)
QEMU  := qemu-system-i386

# Freestanding: no C library and no operating system under us. We ARE the operating system.
CFLAGS  := --target=i686-elf -std=gnu11 -ffreestanding -fno-stack-protector -fno-pic -fno-builtin \
           -mgeneral-regs-only -fno-asynchronous-unwind-tables -O2 -g -Wall -Wextra -Isrc
ASFLAGS := --target=i686-elf -fno-pic
LDFLAGS := -m elf_i386 -T linker.ld -nostdlib -z max-page-size=0x1000

SRC := $(wildcard src/*.c src/*.S)
OBJ := $(patsubst src/%,build/%.o,$(SRC))
QEMU_FLAGS := -kernel build/kernel.elf -m 128M -no-reboot

all: build/kernel.elf

build:
	mkdir -p build

build/%.c.o: src/%.c $(wildcard src/*.h) | build
	$(CLANG) $(CFLAGS) -c $< -o $@

build/%.S.o: src/%.S | build
	$(CLANG) $(ASFLAGS) -c $< -o $@

build/kernel.elf: $(OBJ) linker.ld
	$(LLD) $(LDFLAGS) -o $@ $(OBJ)
	@echo "Built $@. Start it with: make run"

run: build/kernel.elf
	$(QEMU) $(QEMU_FLAGS) -serial stdio

run-text: build/kernel.elf
	$(QEMU) $(QEMU_FLAGS) -display curses

run-serial: build/kernel.elf
	$(QEMU) $(QEMU_FLAGS) -display none -serial stdio

clean:
	rm -rf build

.PHONY: all run run-text run-serial clean
