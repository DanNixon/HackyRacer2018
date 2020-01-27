#include "relay.hpp"

#include <Arduino.h>

relay::relay(int const pin)
    : m_pin(pin) {
}

void relay::init() {
  pinMode(m_pin, OUTPUT);
  off();
}

void relay::on() {
  digitalWrite(m_pin, LOW);
}

void relay::off() {
  digitalWrite(m_pin, HIGH);
}
