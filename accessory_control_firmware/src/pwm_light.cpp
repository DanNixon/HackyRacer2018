#include "pwm_light.hpp"

#include <Arduino.h>

pwm_light::pwm_light(int const pin, int const low_level, int const high_level)
    : m_pin(pin)
    , m_low_level(low_level)
    , m_high_level(high_level) {
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
  case level::low:
    v = m_low_level;
    break;
  case level::high:
    v = m_high_level;
    break;
  default:
    return;
  }
  analogWrite(m_pin, v);
}
