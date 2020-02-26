#include <Arduino.h>

#include "device/button.hpp"
#include "device/led.hpp"
#include "device/relay.hpp"
#include "device/three_position_switch.hpp"
#include "logic/lights.hpp"
#include "logic/motor.hpp"
#include "pins.hpp"

device::relay horn(pins::horn_relay);

device::three_position_switch gear_switch(pins::gear_switch_a,
                                          pins::gear_switch_b);
device::three_position_switch lights_switch(pins::lights_switch_a,
                                            pins::lights_switch_b);

device::button brake_pedal_button(pins::break_pedal_switch);
device::button full_beam_button(pins::blue_button);
device::button horn_button(pins::red_button);

void power_on_sanity_check();

using position = device::three_position_switch::position;
using light_role = logic::lights::role;

void setup() {
  Serial.begin(9600);
  Serial.println("Hello");

  device::led::init();
  logic::motor::init();
  logic::lights::init();

  horn.init();

  gear_switch.init();
  lights_switch.init();

  brake_pedal_button.init();
  full_beam_button.init();
  horn_button.init();

  power_on_sanity_check();
}

void loop() {
  using action = device::button::action;

  if (gear_switch.update()) {
    switch (gear_switch.pos()) {
    case position::A:
      Serial.println("Gear: drive");
      logic::motor::set_drive();
      logic::motor::enable();
      logic::lights::clear_role(light_role::reverse);
      break;
    case position::B:
      Serial.println("Gear: neutral");
      logic::motor::disable();
      logic::lights::clear_role(light_role::reverse);
      break;
    case position::C:
      Serial.println("Gear: reverse");
      logic::motor::set_reverse();
      logic::motor::enable();
      logic::lights::set_role(light_role::reverse);
      break;
    default:
      break;
    }
    logic::lights::output();
  }

  if (lights_switch.update()) {
    switch (lights_switch.pos()) {
    case position::A:
      Serial.println("Lights: off");
      logic::lights::clear_role(light_role::headlights);
      logic::lights::clear_role(light_role::headlights_full);
      break;
    case position::B:
      Serial.println("Lights: headlights");
      logic::lights::set_role(light_role::headlights);
      logic::lights::clear_role(light_role::headlights_full);
      break;
    case position::C:
      Serial.println("Light: full beam");
      logic::lights::set_role(light_role::headlights);
      logic::lights::set_role(light_role::headlights_full);
      break;
    default:
      break;
    }
    logic::lights::output();
  }

  if (full_beam_button.update()) {
    switch (full_beam_button.state()) {
    case action::pressed:
      Serial.println("Light: full beam (button - on)");
      logic::lights::set_role(light_role::headlights_full_momentary);
      break;
    case action::released_short:
    case action::released_long:
      Serial.println("Light: full beam (button - off)");
      logic::lights::clear_role(light_role::headlights_full_momentary);
      break;
    default:
      break;
    }
    logic::lights::output();
  }

  if (brake_pedal_button.update()) {
    switch (brake_pedal_button.state()) {
    case action::pressed:
      Serial.println("Brake: on");
      logic::lights::set_role(light_role::brake);
      break;
    case action::released_short:
    case action::released_long:
      Serial.println("Brake: off");
      logic::lights::clear_role(light_role::brake);
      break;
    default:
      break;
    }
    logic::lights::output();
  }

  if (horn_button.update()) {
    switch (horn_button.state()) {
    case action::pressed:
      Serial.println("Horn: on");
      horn.on();
      break;
    case action::released_short:
    case action::released_long:
      Serial.println("Horn: off");
      horn.off();
      break;
    default:
      break;
    }
  }
}

void power_on_sanity_check() {
  logic::lights::set_role(light_role::headlights);
  logic::lights::set_role(light_role::headlights_full);
  logic::lights::set_role(light_role::brake);
  logic::lights::output();

  /* Wait for switch to be in neutral position */
  while (gear_switch.pos() != position::B) {
    delay(10);
    gear_switch.update();
  }

  logic::lights::clear_all_roles();
  logic::lights::output();
}
