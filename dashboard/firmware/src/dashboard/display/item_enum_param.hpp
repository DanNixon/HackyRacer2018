#pragma once

#include "dashboard/device/tft.h"
#include "dashboard/value/enum.hpp"
#include "item.hpp"

namespace dashboard
{
namespace display
{
  class EnumParameterItem : public Item<1>
  {
  private:
    static constexpr int position_button = 205;

  public:
    EnumParameterItem(value::EnumValue *value)
        : m_value(value)
    {
    }

    virtual void render(bool full, int yOffset) const
    {
      constexpr auto valueXOffset(80);

      const auto y(yOffset + 4);

      device::tft.setTextColor(ILI9341_WHITE, ILI9341_BLACK);
      device::tft.setTextSize(2);

      if (full)
      {
        /* Name */
        device::tft.setCursor(2, y);
        device::tft.print(m_value->name());
      }

      if (full || m_value->valueDirty(value::IValue::DIRTY_DISPLAY, true))
      {
        /* Clear existing value from screen */
        device::tft.fillRect(valueXOffset, yOffset, position_button - valueXOffset, row_height,
                             ILI9341_BLACK);

        /* Value */
        device::tft.setCursor(valueXOffset, y);
        device::tft.print(m_value->to_string().c_str());
      }

      if (full)
      {
        device::tft.setTextColor(ILI9341_BLUE, ILI9341_BLACK);
        device::tft.setCursor(position_button, yOffset + 4);
        device::tft.print("<>");
      }
    }

    virtual void handleTouch(int x, int y) const
    {
      if (x >= position_button)
      {
        m_value->advanceToNextState();
      }
    }

  private:
    value::EnumValue *m_value;
  };
}
}
