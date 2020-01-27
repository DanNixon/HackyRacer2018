#include "motor.hpp"

#include "relay.hpp"

relay reverse_signal(5);
relay pot_high_side(4);

namespace motor {
void init() {
  reverse_signal.init();
  pot_high_side.init();
}

void enable() {
  pot_high_side.on();
}

void disable() {
  pot_high_side.off();
}

void set_drive() {
  reverse_signal.off();
}

void set_reverse() {
  reverse_signal.on();
}
} // namespace motor
