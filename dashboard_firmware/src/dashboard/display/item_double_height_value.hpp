#pragma once

#include "dashboard/device/tft.h"
#include "dashboard/value/numeric.hpp"
#include "item.hpp"

namespace dashboard
{
namespace display
{
  class DoubleHeightValueItem : public Item<2>
  {
  public:
    DoubleHeightValueItem(value::IValue *value)
        : m_value(value)
    {
    }

    virtual void render(bool full, int yOffset) const
    {
      const auto y(yOffset + 4);

      /* If state has changed then need to do a full redraw to get text colour
       * change */
      if (m_value->stateDirty(value::IValue::DIRTY_DISPLAY, true))
      {
        full = true;
      }

      /* Set text colour for state */
      switch (m_value->state())
      {
      case value::IValue::WARN:
        device::tft.setTextColor(ILI9341_YELLOW, ILI9341_BLACK);
        break;
      case value::IValue::CRITICAL:
        device::tft.setTextColor(ILI9341_RED, ILI9341_BLACK);
        break;
      default:
        device::tft.setTextColor(ILI9341_WHITE, ILI9341_BLACK);
        break;
      }

      if (full)
      {
        device::tft.setTextSize(2);

        /* Name */
        device::tft.setCursor(2, y);
        device::tft.print(m_value->name());
      }

      if (full || m_value->valueDirty(value::IValue::DIRTY_DISPLAY, true))
      {
        device::tft.setTextSize(5);

        /* Value */
        device::tft.setCursor(28, y + 24);
        device::tft.print(m_value->to_string().c_str());
      }
    }

  private:
    value::IValue *m_value;
  };
}
}
