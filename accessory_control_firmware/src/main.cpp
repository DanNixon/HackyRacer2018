#include <Arduino.h>

#include "button.hpp"
#include "led.hpp"
#include "motor.hpp"
#include "pwm_light.hpp"
#include "relay.hpp"
#include "three_pos_switch.hpp"

pwm_light front_white(8);
pwm_light front_high_intensity(9);
pwm_light rear_white(10);
pwm_light rear_red(11);

relay horn(7);

three_pos_switch direction_sw(A1, A0);
three_pos_switch lights_sw(A2, A3);
button brake_sw(A5);
button horn_sw(0); // TODO

void setup() {
  Serial.begin(9600);

  led_init();
  motor_init();

  front_white.init();
  front_high_intensity.init();
  rear_white.init();
  rear_red.init();

  horn.init();

  direction_sw.init();
  lights_sw.init();
  brake_sw.init();
  horn_sw.init();
}

void loop() {
  using position = three_pos_switch::position;
  using action = button::action;
  using level = pwm_light::level;

  if (direction_sw.update()) {
    switch (direction_sw.pos()) {
    case position::A:
      Serial.println("Gear: drive");
      motor_enable();
      rear_white.set(level::off);
      motor_set_drive();
      break;
    case position::B:
      Serial.println("Gear: neutral");
      motor_disable();
      rear_white.set(level::off);
      break;
    case position::C:
      Serial.println("Gear: reverse");
      motor_enable();
      rear_white.set(level::medium);
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
      front_white.set(level::off);
      rear_red.set(level::off);
      front_high_intensity.set(level::off);
      break;
    case position::B:
      Serial.println("Lights: headlights");
      front_white.set(level::medium);
      rear_red.set(level::medium);
      front_high_intensity.set(level::off);
      break;
    case position::C:
      Serial.println("Light: full beam");
      front_white.set(level::medium);
      rear_red.set(level::medium);
      front_high_intensity.set(level::full);
      break;
    default:
      break;
    }
  }

  if (brake_sw.update()) {
    switch (brake_sw.state()) {
    case action::Pressed:
      Serial.println("Brake: on");
      rear_red.set(level::full);
      break;
    case action::Released:
      Serial.println("Brake: off");
      rear_red.set(lights_sw.pos() == position::A ? level::off : level::medium);
      break;
    default:
      break;
    }
  }

  if (horn_sw.update()) {
    switch (horn_sw.state()) {
    case action::Pressed:
      Serial.println("Horn: on");
      horn.on();
      break;
    case action::Released:
      Serial.println("Horn: off");
      horn.off();
      break;
    default:
      break;
    }
  }
}
