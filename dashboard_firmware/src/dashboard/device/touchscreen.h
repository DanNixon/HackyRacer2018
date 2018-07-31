#pragma once

#include <inttypes.h>

namespace dashboard
{
namespace device
{
  struct TouchscreenCalibration
  {
    int32_t xMin;
    int32_t yMin;
    int32_t xMax;
    int32_t yMax;
  };

  struct TouchscreenPoint
  {
    int32_t x;
    int32_t y;
  };

  void touchscreenInit();
  bool touchscreenUpdate(TouchscreenPoint &point);
}
}
