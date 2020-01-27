#include "button.hpp"

#include <Arduino.h>

constexpr auto debounce_time_ms = 25;

button::button(int const pin, unsigned long const long_press_time_ms)
    : m_pin(pin)
    , m_long_press_time_ms(long_press_time_ms)
    , m_state(action::unknown)
    , m_last_state_change(0) {
}

void button::init() {
  pinMode(m_pin, INPUT_PULLUP);
}

bool button::update() {
  auto const now = millis();
  auto const delta_t = now - m_last_state_change;

  if (delta_t < debounce_time_ms) {
    return false;
  }

  auto const button_is_down = digitalRead(m_pin) == LOW;
  bool changed = false;

  if (m_state != action::pressed && button_is_down) {
    changed = true;
    m_state = action::pressed;
  } else if (m_state == action::pressed && !button_is_down) {
    changed = true;
    m_state = delta_t > m_long_press_time_ms ? action::released_long
                                             : action::released_short;
  }

  if (changed) {
    m_last_state_change = now;
  }

  return changed;
}

button::action button::state() const {
  return m_state;
}
