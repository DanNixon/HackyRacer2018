#include <Arduino.h>

#include "button.hpp"
#include "led.hpp"
#include "motor.hpp"
#include "relay.hpp"
#include "three_pos_switch.hpp"

relay brake_lights(11);
relay reverse_lights(10);
relay rear_lights(9);
relay headlights(8);
relay full_beam(7);

three_pos_switch direction_sw(A1, A0);
three_pos_switch lights_sw(A2, A3);
button brake_sw(A5);

void setup() {
  Serial.begin(9600);

  led_init();
  motor_init();

  brake_lights.init();
  reverse_lights.init();
  rear_lights.init();
  headlights.init();
  full_beam.init();

  direction_sw.init();
  lights_sw.init();
  brake_sw.init();
}

void loop() {
  using position = three_pos_switch::position;
  using action = button::action;

  if (direction_sw.update()) {
    switch (direction_sw.pos()) {
    case position::A:
      Serial.println("Gear: drive");
      motor_enable();
      reverse_lights.off();
      motor_set_drive();
      break;
    case position::B:
      Serial.println("Gear: neutral");
      motor_disable();
      reverse_lights.off();
      break;
    case position::C:
      Serial.println("Gear: reverse");
      motor_enable();
      reverse_lights.on();
      motor_set_reverse();
      break;
    default:
      break;
    }
  }

  if (lights_sw.update()) {
    switch (lights_sw.pos()) {
    case position::A:
      Serial.println("Lights: off");
      rear_lights.off();
      headlights.off();
      full_beam.off();
      break;
    case position::B:
      Serial.println("Lights: headlights");
      rear_lights.on();
      headlights.on();
      full_beam.off();
      break;
    case position::C:
      Serial.println("Light: full beam");
      rear_lights.on();
      headlights.on();
      full_beam.on();
      break;
    default:
      break;
    }
  }

  if (brake_sw.update()) {
    switch (brake_sw.state()) {
    case action::Pressed:
      Serial.println("Brake: on");
      brake_lights.on();
      break;
    case action::Released:
      Serial.println("Brake: off");
      brake_lights.off();
      break;
    default:
      break;
    }
  }
}
