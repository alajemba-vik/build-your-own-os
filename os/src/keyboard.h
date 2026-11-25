/* keyboard.h: the PS/2 keyboard, plus one place to read keys from (keyboard or serial port). */
#ifndef KEYBOARD_H
#define KEYBOARD_H
#define KEY_ESC   27
#define KEY_UP    0x80
#define KEY_DOWN  0x81
#define KEY_LEFT  0x82
#define KEY_RIGHT 0x83
void keyboard_init(void);
unsigned keyboard_presses(void);
int input_poll(void);   /* the next key, or -1 if none: never waits */
int input_getc(void);   /* waits for a key */
#endif
