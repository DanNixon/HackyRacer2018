#include "led.hpp"

#include <Arduino.h>

constexpr auto led_pin = 13;

void led_init() {
  pinMode(led_pin, OUTPUT);
  led_off();
}

void led_on() {
  digitalWrite(led_pin, HIGH);
}

void led_off() {
  digitalWrite(led_pin, LOW);
}
