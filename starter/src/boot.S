/* boot.S: the very first code that runs.
   QEMU (or GRUB) looks for the "multiboot header" below, loads our kernel at 1 MiB,
   and jumps to _start with the CPU already in 32-bit mode. We set up a stack and call C. */

.set ALIGN,    1 << 0              /* load modules on page boundaries */
.set MEMINFO,  1 << 1              /* please give us a map of the memory */
.set FLAGS,    ALIGN | MEMINFO
.set MAGIC,    0x1BADB002          /* the number the bootloader looks for */
.set CHECKSUM, -(MAGIC + FLAGS)    /* MAGIC + FLAGS + CHECKSUM must be 0 */

.section .multiboot, "a"
.align 4
.long MAGIC
.long FLAGS
.long CHECKSUM

.section .bss
.align 16
stack_bottom:
.skip 16384                        /* 16 KiB of stack for our C code */
stack_top:

.section .text
.global _start
.type _start, @function
_start:
    mov $stack_top, %esp           /* the stack grows down, so start at the top */
    sub $8, %esp                   /* keep the stack 16-byte aligned for C */
    push %ebx                      /* 2nd argument: where the bootloader put its info */
    push %eax                      /* 1st argument: the magic number 0x2BADB002 */
    call kernel_main
    cli                            /* if kernel_main ever returns: stop forever */
1:  hlt
    jmp 1b
