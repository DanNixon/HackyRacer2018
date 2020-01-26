#include "led.hpp"

#include <Arduino.h>

constexpr auto led_pin = 13;

namespace led {
void init() {
  pinMode(led_pin, OUTPUT);
  off();
}

void on() {
  digitalWrite(led_pin, HIGH);
}

void off() {
  digitalWrite(led_pin, LOW);
}
} // namespace led
