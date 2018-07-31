#include "touchscreen.h"

#include <cmath>

#include <ILI9341_t3.h>
#include <XPT2046_Touchscreen.h>
#undef round

#include "pin_config.h"
#include "tft.h"

namespace dashboard
{
namespace device
{
  constexpr auto DEBOUNCE(50);
  constexpr TouchscreenCalibration CALIBRATION{205, 188, 3633, 3622};

  XPT2046_Touchscreen touchscreen(TOUCH_CS, TOUCH_IRQ);

  bool lastTouched(false);
  uint32_t lastTouchTime(0);

  bool touchscreenPoll()
  {
    bool touched(false);

    if (touchscreen.tirqTouched())
    {
      const bool touchscreenReportsTouched(touchscreen.touched());
      const auto now(millis());

      if (!lastTouched && touchscreenReportsTouched && (lastTouchTime < now - DEBOUNCE))
      {
        touched = true;
        lastTouched = true;
        lastTouchTime = now;
      }
      else if (lastTouched && !touchscreenReportsTouched)
      {
        touched = false;
        lastTouched = false;
      }
    }

    return touched;
  }

  void touchscreenApplyCalibration(TouchscreenPoint &point)
  {
    static constexpr auto xSlope((float)(ILI9341_TFTWIDTH - 1) /
                                 (CALIBRATION.xMax - CALIBRATION.xMin));
    static constexpr auto ySlope((float)(ILI9341_TFTHEIGHT - 1) /
                                 (CALIBRATION.yMax - CALIBRATION.yMin));

    if (point.x > CALIBRATION.xMax)
    {
      point.x = ILI9341_TFTWIDTH - 1;
    }
    else if (point.x < CALIBRATION.xMin)
    {
      point.x = 0;
    }
    else
    {
      point.x = std::round(xSlope * (point.x - CALIBRATION.xMin));
    }

    if (point.y > CALIBRATION.yMax)
    {
      point.y = ILI9341_TFTHEIGHT - 1;
    }
    else if (point.y < CALIBRATION.yMin)
    {
      point.y = 0;
    }
    else
    {
      point.y = std::round(ySlope * (point.y - CALIBRATION.yMin));
    }
  }

  void touchscreenInit()
  {
    touchscreen.begin();
    touchscreen.setRotation(2);
  }

  bool touchscreenUpdate(TouchscreenPoint &point)
  {
    if (touchscreenPoll())
    {
      const auto p = touchscreen.getPoint();
      point.x = p.x;
      point.y = p.y;

      touchscreenApplyCalibration(point);

      return true;
    }

    return false;
  }
}
}
