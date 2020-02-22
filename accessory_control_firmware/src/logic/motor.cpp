#include "motor.hpp"

#include "device/relay.hpp"
#include "pins.hpp"

device::relay reverse_signal(pins::reverse_relay);
device::relay pot_high_side(pins::pot_high_side_relay);

namespace logic {
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
} // namespace logic
