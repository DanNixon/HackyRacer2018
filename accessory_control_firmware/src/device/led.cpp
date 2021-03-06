#include "led.hpp"

#include <Arduino.h>

constexpr auto led_pin = 13;

namespace device {
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

void toggle() {
  digitalWrite(led_pin, !digitalRead(led_pin));
}
} // namespace led
} // namespace device
