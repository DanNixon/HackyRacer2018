#pragma once

/* SPI */
/* MOSI 11 */
/* MISO 12 */
/* SCLK 13 */

namespace pins {
constexpr auto tft_cs = 10;
constexpr auto tft_dc = 9;
constexpr auto tft_reset = 8;

constexpr auto &gps_serial = Serial4;
} // namespace pins
