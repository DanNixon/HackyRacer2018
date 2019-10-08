#include "button.hpp"

#include <Arduino.h>

constexpr auto debounce_time_ms = 25;

button::button(int const pin)
    : m_pin(pin)
    , m_state(action::Unknown)
    , m_last_state_change(0) {
}

void button::init() {
  pinMode(m_pin, INPUT_PULLUP);
}

bool button::update() {
  auto const now = millis();
  if (now - m_last_state_change < debounce_time_ms) {
    return false;
  }

  auto const new_state =
      digitalRead(m_pin) == LOW ? action::Pressed : action::Released;
  auto const changed = new_state != m_state;

  m_state = new_state;
  m_last_state_change = now;

  return changed;
}

button::action button::state() const {
  return m_state;
}
