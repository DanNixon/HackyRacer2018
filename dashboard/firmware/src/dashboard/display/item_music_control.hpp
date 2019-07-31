#pragma once

#include <font_AwesomeF000.h>

#include "dashboard/device/audio.h"
#include "dashboard/device/tft.h"
#include "item.hpp"

namespace dashboard
{
namespace display
{
  class MusicControlItem : public Item<1>
  {
  private:
    static constexpr int position_previous = 2;
    static constexpr int position_play = 95;
    static constexpr int position_next = 210;

  public:
    MusicControlItem()
    {
    }

    virtual void render(bool full, int yOffset) const
    {
      device::tft.setTextSize(3);

      if (full)
      {
        device::tft.setFont(AwesomeF000_18);

        device::tft.setTextColor(ILI9341_BLUE, ILI9341_BLACK);
        device::tft.setCursor(position_previous, yOffset + 4);
        device::tft.drawFontChar(73);

        device::tft.setTextColor(ILI9341_BLUE, ILI9341_BLACK);
        device::tft.setCursor(position_next, yOffset + 4);
        device::tft.drawFontChar(80);

        device::tft.setFontAdafruit();
      }

      device::tft.setFont(AwesomeF000_18);
      device::tft.setCursor(position_play, yOffset + 4);
      if (device::audioMusicPlaying())
      {
        device::tft.setTextColor(ILI9341_RED, ILI9341_BLACK);
        device::tft.drawFontChar(77);
      }
      else
      {
        device::tft.setTextColor(ILI9341_GREEN, ILI9341_BLACK);
        device::tft.drawFontChar(75);
      }
      device::tft.setFontAdafruit();
    }

    virtual void handleTouch(int x, int y) const
    {
      constexpr auto box(64);

      if (x >= position_previous && x <= position_previous + box)
      {
        device ::audioMusicPrevious();
      }
      else if (x >= position_play && x <= position_play + box)
      {
        if (device::audioMusicPlaying())
        {
          device::audioMusicStop();
        }
        else
        {
          device ::audioMusicNext();
        }
      }
      else if (x >= position_previous && x <= position_next + box)
      {
        device ::audioMusicNext();
      }
    };
  };
} // namespace display
} // namespace dashboard
