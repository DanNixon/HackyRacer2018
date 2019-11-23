#include "pwm_light.hpp"

#include <Arduino.h>

pwm_light::pwm_light(int const pin)
    : m_pin(pin) {
}

void pwm_light::init() {
  pinMode(m_pin, OUTPUT);
  set(level::off);
}

void pwm_light::set(level const l) {
  int v;
  switch (l) {
  case level::off:
    v = 0;
    break;
  case level::medium:
    v = 127;
    break;
  case level::full:
    v = 255;
    break;
  default:
    return;
  }
  analogWrite(m_pin, v);
}
