#include "motor.hpp"

#include "relay.hpp"

relay reverse_signal(5);
relay pot_high_side(4);

void motor_init() {
  reverse_signal.init();
  pot_high_side.init();
}

void motor_enable() {
  pot_high_side.on();
}

void motor_disable() {
  pot_high_side.off();
}

void motor_set_drive() {
  reverse_signal.off();
}

void motor_set_reverse() {
  reverse_signal.on();
}
