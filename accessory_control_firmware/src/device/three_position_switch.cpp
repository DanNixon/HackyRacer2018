#include "three_position_switch.hpp"

#include <Arduino.h>

constexpr auto debounce_time_ms = 25;

namespace device {
three_position_switch::three_position_switch(int const pin_1, int const pin_2)
    : m_pin_1(pin_1)
    , m_pin_2(pin_2)
    , m_pin_1_state(false)
    , m_pin_2_state(false)
    , m_last_state_change(0) {
}

void three_position_switch::init() {
  pinMode(m_pin_1, INPUT_PULLUP);
  pinMode(m_pin_2, INPUT_PULLUP);
}

bool three_position_switch::update() {
  auto const now = millis();
  if (millis() - m_last_state_change < debounce_time_ms) {
    return false;
  }

  bool const pin_1_new_state = digitalRead(m_pin_1) == LOW;
  bool const pin_2_new_state = digitalRead(m_pin_2) == LOW;

  bool changed = false;

  if (m_last_state_change > 0) {
    changed = (pin_1_new_state != m_pin_1_state) ||
              (pin_2_new_state != m_pin_2_state);
  } else {
    changed = true;
  }

  m_pin_1_state = pin_1_new_state;
  m_pin_2_state = pin_2_new_state;

  if (changed) {
    m_last_state_change = now;
  }

  return changed;
}

three_position_switch::position three_position_switch::pos() const {
  if (m_last_state_change == 0) {
    return position::Unknown;
  } else if (m_pin_1_state && !m_pin_2_state) {
    return position::A;
  } else if (!m_pin_1_state && !m_pin_2_state) {
    return position::B;
  } else if (!m_pin_1_state && m_pin_2_state) {
    return position::C;
  }
  return position::Unknown;
}
} // namespace device
