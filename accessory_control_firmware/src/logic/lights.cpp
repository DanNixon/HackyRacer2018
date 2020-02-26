#include "lights.hpp"

#include "device/pwm_light.hpp"
#include "pins.hpp"

constexpr auto role_count = 5;
bool role_enable[role_count];

device::pwm_light front_white(pins::front_white_lights, 10);
device::pwm_light front_white_bright(pins::front_white_bright_lights, 100, 255);
device::pwm_light rear_white(pins::rear_white_lights, 25);
device::pwm_light rear_red(pins::rear_red_lights, 20, 255);

namespace logic {
namespace lights {
void init() {
  front_white.init();
  front_white_bright.init();
  rear_white.init();
  rear_red.init();

  clear_all_roles();
  output();
}

void set_role(role const r) {
  role_enable[static_cast<int>(r)] = true;
}

void clear_role(role const r) {
  role_enable[static_cast<int>(r)] = false;
}

void clear_all_roles() {
  for (auto i = 0; i < role_count; i++) {
    role_enable[i] = false;
  }
}

bool role_is_enabled(role const r) {
  return role_enable[static_cast<int>(r)];
}

void output() {
  using level = device::pwm_light::level;

  level front_white_level = level::off;
  level front_white_bright_level = level::off;
  level rear_white_level = level::off;
  level rear_red_level = level::off;

  if (role_is_enabled(role::headlights)) {
    front_white_level = level::on;
    rear_red_level = level::low;
  }
  if (role_is_enabled(role::headlights_full) ||
      role_is_enabled(role::headlights_full_momentary)) {
    front_white_bright_level = level::on;
  }
  if (role_is_enabled(role::reverse)) {
    rear_white_level = level::on;
  }
  if (role_is_enabled(role::brake)) {
    rear_red_level = level::high;
  }

  front_white.set(front_white_level);
  front_white_bright.set(front_white_bright_level);
  rear_white.set(rear_white_level);
  rear_red.set(rear_red_level);
}
} // namespace lights
} // namespace logic
