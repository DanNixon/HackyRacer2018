#pragma once

#include "dashboard/device/tft.h"
#include "dashboard/value/numeric_units.hpp"
#include "item.hpp"

namespace dashboard
{
namespace display
{
  class VolumeControlItem : public Item<1>
  {
  private:
    static constexpr float delta = 0.05;
    static constexpr int position_minus = 180;
    static constexpr int position_plus = 210;

  public:
    VolumeControlItem(value ::VolumeValue *value)
        : m_value(value)
    {
    }

    virtual void render(bool full, int yOffset) const
    {
      constexpr auto valueXOffset(80);

      const auto y(yOffset + 4);

      device::tft.setTextColor(ILI9341_WHITE, ILI9341_BLACK);

      if (full)
      {
        device::tft.setTextSize(2);

        /* Name */
        device::tft.setCursor(2, y);
        device::tft.print(m_value->name());
      }

      if (full || m_value->valueDirty(value::IValue::DIRTY_DISPLAY, true))
      {
        device::tft.setTextSize(3);

        /* Value */
        device::tft.setCursor(valueXOffset, y);
        device::tft.print(m_value->to_string().c_str());
      }

      if (full)
      {
        device::tft.setTextColor(ILI9341_RED, ILI9341_BLACK);
        device::tft.setCursor(position_minus, yOffset + 4);
        device::tft.print("-");

        device::tft.setTextColor(ILI9341_GREEN, ILI9341_BLACK);
        device::tft.setCursor(position_plus, yOffset + 4);
        device::tft.print("+");
      }
    }

    virtual void handleTouch(int x, int y) const
    {
      if (x >= position_minus && x < position_plus)
      {
        m_value->setValue(std::max(0.0f, m_value->value() - delta));
      }
      else if (x >= position_plus)
      {
        m_value->setValue(m_value->value() + delta);
      }
    }

  private:
    value::VolumeValue *m_value;
  };
}
}
