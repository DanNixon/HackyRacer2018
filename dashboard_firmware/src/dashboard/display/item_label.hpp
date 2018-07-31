#pragma once

#include "dashboard/device/tft.h"
#include "item.hpp"

namespace dashboard
{
namespace display
{
  class LabelItem : public Item<1>
  {
  public:
    LabelItem(const std::string &text, unsigned int textSize = 3)
        : m_text(text)
        , m_textSize(textSize)
    {
    }

    virtual void render(bool full, int yOffset) const
    {
      if (full || m_dirty)
      {
        device::tft.setTextColor(ILI9341_WHITE, ILI9341_BLACK);
        device::tft.setTextSize(m_textSize);
        device::tft.setCursor(2, yOffset + 4);
        device::tft.print(m_text.c_str());
      }
    }

    void setText(const std::string &text)
    {
      m_dirty = true;
      m_text = text;
    }

  private:
    std::string m_text;
    unsigned int m_textSize;
    bool m_dirty;
  };
}
}
