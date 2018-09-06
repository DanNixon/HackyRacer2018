#include "tft.h"

#include "pin_config.h"

namespace dashboard
{
namespace device
{
  ILI9341_t3 tft = ILI9341_t3(TFT_CS, TFT_DC, TFT_RESET);

  void tftInit()
  {
    tft.begin();
    tft.setTextWrap(false);
    tft.fillScreen(ILI9341_BLACK);
  }
}
}
