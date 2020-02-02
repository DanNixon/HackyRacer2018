#include <ILI9341_t3.h>
#include <SD.h>
#undef swap

#include "value/value.hpp"

/* SPI */
/* MOSI 11 */
/* MISO 12 */
/* SCLK 13 */
ILI9341_t3 tft(tft_cs, tft_dc, tft_reset);

void setup() {
  Serial.begin(9600);
  /* while (!Serial) */
  {}
  Serial.println("Hello");

  /* SD card */
  const bool sd_card_ok(SD.begin(BUILTIN_SDCARD));
  Serial.print("SD card OK: ");
  Serial.println(sd_card_ok);

  /* TFT display */
  tft.begin();
  tft.setTextWrap(false);
  tft.setRotation(1);
  tft.fillScreen(ILI9341_BLACK);

  /* TODO */
  tft.print("test");
}

void loop(void) {
  /* TODO */
}
