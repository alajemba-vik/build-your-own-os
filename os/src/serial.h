/* serial.h: the serial port (COM1). Everything we print also goes here,
   so you can read it in your terminal and an automatic test can check it. */
#ifndef SERIAL_H
#define SERIAL_H
void serial_init(void);
void serial_putc(char c);
int serial_getc(void);   /* -1 if nothing was typed */
#endif
