/* cpu.S: the few things C cannot do: load the GDT and IDT tables,
   and the small entry points ("stubs") the CPU jumps to on every interrupt. */

.section .text

/* void gdt_flush(struct gdt_ptr *p): load the GDT and reload every segment register */
.global gdt_flush
gdt_flush:
    movl 4(%esp), %eax
    lgdt (%eax)
    movw $0x10, %ax                /* 0x10 = our data segment (entry 2) */
    movw %ax, %ds
    movw %ax, %es
    movw %ax, %fs
    movw %ax, %gs
    movw %ax, %ss
    ljmp $0x08, $.Lreload_cs       /* 0x08 = our code segment (entry 1) */
.Lreload_cs:
    ret

/* void idt_load(struct idt_ptr *p) */
.global idt_load
idt_load:
    movl 4(%esp), %eax
    lidt (%eax)
    ret

/* Every stub pushes the same shape (an error code, then its number) so one C function can handle them all. */
.macro ISR_NOERR num
.global isr\num
isr\num:
    pushl $0                       /* this one has no error code: push a fake 0 */
    pushl $\num
    jmp isr_common
.endm

.macro ISR_ERR num
.global isr\num
isr\num:
    pushl $\num                    /* the CPU already pushed an error code */
    jmp isr_common
.endm

ISR_NOERR 0
ISR_NOERR 1
ISR_NOERR 2
ISR_NOERR 3
ISR_NOERR 4
ISR_NOERR 5
ISR_NOERR 6
ISR_NOERR 7
ISR_ERR   8
ISR_NOERR 9
ISR_ERR   10
ISR_ERR   11
ISR_ERR   12
ISR_ERR   13
ISR_ERR   14
ISR_NOERR 15
ISR_NOERR 16
ISR_ERR   17
ISR_NOERR 18
ISR_NOERR 19
ISR_NOERR 20
ISR_ERR   21
ISR_NOERR 22
ISR_NOERR 23
ISR_NOERR 24
ISR_NOERR 25
ISR_NOERR 26
ISR_NOERR 27
ISR_NOERR 28
ISR_ERR   29
ISR_ERR   30
ISR_NOERR 31
/* 32-47: the 16 hardware interrupts (IRQ 0-15) after we moved them with the PIC */
ISR_NOERR 32
ISR_NOERR 33
ISR_NOERR 34
ISR_NOERR 35
ISR_NOERR 36
ISR_NOERR 37
ISR_NOERR 38
ISR_NOERR 39
ISR_NOERR 40
ISR_NOERR 41
ISR_NOERR 42
ISR_NOERR 43
ISR_NOERR 44
ISR_NOERR 45
ISR_NOERR 46
ISR_NOERR 47

isr_common:
    pushal                         /* save every general register */
    pushl %ds
    pushl %es
    pushl %fs
    pushl %gs
    movw $0x10, %ax
    movw %ax, %ds
    movw %ax, %es
    movw %ax, %fs
    movw %ax, %gs
    pushl %esp                     /* argument: pointer to everything we saved (struct regs) */
    call isr_handler
    addl $4, %esp
    popl %gs
    popl %fs
    popl %es
    popl %ds
    popal
    addl $8, %esp                  /* drop the number and the error code */
    iret                           /* go back to what was running */

.section .rodata
.align 4
.global isr_stub_table
isr_stub_table:
    .long isr0,  isr1,  isr2,  isr3,  isr4,  isr5,  isr6,  isr7
    .long isr8,  isr9,  isr10, isr11, isr12, isr13, isr14, isr15
    .long isr16, isr17, isr18, isr19, isr20, isr21, isr22, isr23
    .long isr24, isr25, isr26, isr27, isr28, isr29, isr30, isr31
    .long isr32, isr33, isr34, isr35, isr36, isr37, isr38, isr39
    .long isr40, isr41, isr42, isr43, isr44, isr45, isr46, isr47
