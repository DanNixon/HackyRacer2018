#pragma once

#include <ILI9341_t3.h>
#undef swap

namespace dashboard
{
namespace device
{
  extern ILI9341_t3 tft;

  void tftInit();
}
}
