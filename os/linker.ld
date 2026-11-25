/* linker.ld: where each part of the kernel goes in memory. We start at 1 MiB,
   because the first megabyte holds the BIOS, the VGA screen and other old PC things. */
ENTRY(_start)

SECTIONS
{
    . = 1M;

    .text : ALIGN(4K)
    {
        *(.multiboot)          /* must be near the start of the file */
        *(.text .text.*)
    }
    .rodata : ALIGN(4K) { *(.rodata .rodata.*) }
    .data : ALIGN(4K) { *(.data .data.*) }
    .bss : ALIGN(4K) { *(COMMON) *(.bss .bss.*) }

    kernel_end = .;

    /DISCARD/ : { *(.comment) *(.note .note.*) *(.eh_frame*) }
}
