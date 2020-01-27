#include <Arduino.h>

#include "button.hpp"
#include "led.hpp"
#include "lights.hpp"
#include "motor.hpp"
#include "pins.hpp"
#include "relay.hpp"
#include "three_position_switch.hpp"

relay horn(pins::horn_relay);

three_position_switch gear_switch(pins::gear_switch_a, pins::gear_switch_b);
three_position_switch lights_switch(pins::lights_switch_a,
                                    pins::lights_switch_b);

button brake_pedal_button(pins::break_pedal_switch);
button display_button(pins::display_button);
button horn_button(pins::horn_button);

void setup() {
  Serial.begin(9600);

  led::init();
  motor::init();
  lights::init();

  horn.init();

  gear_switch.init();
  lights_switch.init();

  brake_pedal_button.init();
  display_button.init();
  horn_button.init();
}

void loop() {
  using position = three_position_switch::position;
  using action = button::action;

  if (gear_switch.update()) {
    switch (gear_switch.pos()) {
    case position::A:
      Serial.println("Gear: drive");
      motor::set_drive();
      motor::enable();
      lights::set_role(lights::role::reverse, false);
      break;
    case position::B:
      Serial.println("Gear: neutral");
      motor::disable();
      lights::set_role(lights::role::reverse, false);
      break;
    case position::C:
      Serial.println("Gear: reverse");
      motor::set_reverse();
      motor::enable();
      lights::set_role(lights::role::reverse, true);
      break;
    default:
      break;
    }
    lights::output();
  }

  if (lights_switch.update()) {
    switch (lights_switch.pos()) {
    case position::A:
      Serial.println("Lights: off");
      lights::set_role(lights::role::headlights, false);
      lights::set_role(lights::role::headlights_full, false);
      break;
    case position::B:
      Serial.println("Lights: headlights");
      lights::set_role(lights::role::headlights, true);
      lights::set_role(lights::role::headlights_full, false);
      break;
    case position::C:
      Serial.println("Light: full beam");
      lights::set_role(lights::role::headlights, true);
      lights::set_role(lights::role::headlights_full, true);
      break;
    default:
      break;
    }
    lights::output();
  }

  if (brake_pedal_button.update()) {
    switch (brake_pedal_button.state()) {
    case action::pressed:
      Serial.println("Brake: on");
      lights::set_role(lights::role::brake, true);
      break;
    case action::released_short:
    case action::released_long:
      Serial.println("Brake: off");
      lights::set_role(lights::role::brake, false);
      break;
    default:
      break;
    }
    lights::output();
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
