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
device::button display_button(pins::display_button);
device::button horn_button(pins::horn_button);

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
  display_button.init();
  horn_button.init();
}

void loop() {
  using position = device::three_position_switch::position;
  using action = device::button::action;
  using light_role = logic::lights::role;

  if (gear_switch.update()) {
    switch (gear_switch.pos()) {
    case position::A:
      Serial.println("Gear: drive");
      logic::motor::set_drive();
      logic::motor::enable();
      logic::lights::set_role(light_role::reverse, false);
      break;
    case position::B:
      Serial.println("Gear: neutral");
      logic::motor::disable();
      logic::lights::set_role(light_role::reverse, false);
      break;
    case position::C:
      Serial.println("Gear: reverse");
      logic::motor::set_reverse();
      logic::motor::enable();
      logic::lights::set_role(light_role::reverse, true);
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
      logic::lights::set_role(light_role::headlights, false);
      logic::lights::set_role(light_role::headlights_full, false);
      break;
    case position::B:
      Serial.println("Lights: headlights");
      logic::lights::set_role(light_role::headlights, true);
      logic::lights::set_role(light_role::headlights_full, false);
      break;
    case position::C:
      Serial.println("Light: full beam");
      logic::lights::set_role(light_role::headlights, true);
      logic::lights::set_role(light_role::headlights_full, true);
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
      logic::lights::set_role(light_role::brake, true);
      break;
    case action::released_short:
    case action::released_long:
      Serial.println("Brake: off");
      logic::lights::set_role(light_role::brake, false);
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

  if (display_button.update()) {
    switch (display_button.state()) {
    case action::released_short:
      Serial.println("Display: cycle");
      /* TODO */
      break;
    case action::released_long:
      Serial.println("Display: select");
      /* TODO */
      break;
    default:
      break;
    }
  }
}
