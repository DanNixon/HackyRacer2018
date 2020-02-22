#pragma once

#include <Arduino.h>

namespace pins {
constexpr auto red_button = A5;
constexpr auto blue_button = A1;
constexpr auto green_button = 7;

constexpr auto break_pedal_switch = 8;

constexpr auto gear_switch_a = A4;
constexpr auto gear_switch_b = A0;

constexpr auto lights_switch_a = A2;
constexpr auto lights_switch_b = A3;

constexpr auto horn_relay = 2;
constexpr auto reverse_relay = 3;
constexpr auto pot_high_side_relay = 4;

constexpr auto front_white_lights = 5;
constexpr auto front_white_bright_lights = 6;
constexpr auto rear_white_lights = 9;
constexpr auto rear_red_lights = 10;
} // namespace pins
