#pragma once

#include <FrSkySportSingleWireSerial.h>

/* SPI */
/* MOSI 11 */
/* MISO 12 */
/* SCLK 13 */

/* TFT screen */
constexpr auto TFT_RESET(8);
constexpr auto TFT_DC(9);
constexpr auto TFT_CS(10);

/* Resistive touch screen driver */
constexpr auto TOUCH_CS(14);
constexpr auto TOUCH_IRQ(15);

/* FrSky S.PORT decoder */
constexpr auto SPORT_SERIAL(FrSkySportSingleWireSerial::SERIAL_5);

/* CAN bus */
constexpr auto CAN_BAUD(125000);
constexpr auto CAN_DEVICE(0);
constexpr auto VESC_CAN_ID(2);

/* Horn switch */
constexpr auto HORN_BUTTON_PIN(24);

/* LEDs */
constexpr auto LED_DATA_PIN(23);
