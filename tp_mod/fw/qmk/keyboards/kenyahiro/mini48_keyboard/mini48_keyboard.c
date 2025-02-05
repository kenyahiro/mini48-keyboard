/*
 *
 * ken.yahiro@gmail.com
 */


#include "quantum.h"
#include <stdio.h>


void keyboard_pre_init_kb(void) {
    gpio_set_pin_output(GP8);
    gpio_write_pin_high(GP8);
    wait_ms(10);
    gpio_write_pin_low(GP8);
    keyboard_pre_init_user();
}
