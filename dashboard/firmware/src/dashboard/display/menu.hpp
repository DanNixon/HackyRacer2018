#pragma once

#include <vector>

#include <font_AwesomeF000.h>
#include <font_AwesomeF100.h>

#include "dashboard/device/tft.h"
#include "dashboard/device/touchscreen.h"
#include "screen.hpp"

namespace dashboard
{
namespace display
{
  class Menu
  {
  private:
    using Screens = std::vector<Screen *>;

    static constexpr auto MENU = -1;

  public:
    Menu(const Screens &screens)
        : m_screens(screens)
        , m_currentScreenIdx(MENU)
        , m_lastScreenRender(0)
    {
    }

    void init()
    {
      render(true);
    }

    void update()
    {
      const auto now(millis());

      /* Poll touchscreen */
      device::TouchscreenPoint point;
      if (device::touchscreenUpdate(point))
      {
        handleTouch(point.x, point.y);
      }

      /* Handle rendering */
      if (now - m_lastScreenRender >= 32)
      {
        render(false);
        m_lastScreenRender = now;
      }
    }

  private:
    void setScreen(int screenIdx)
    {
      if (screenIdx != m_currentScreenIdx)
      {
        m_currentScreenIdx = screenIdx;
        render(true);
      }
    }

    void handleTouch(int x, int y)
    {
      if (m_currentScreenIdx == MENU)
      {
        /* Check for main menu item press */
        for (size_t i = 0; i < m_screens.size(); ++i)
        {
          if (y < row_height * (i + 1))
          {
            setScreen(i);
            return;
          }
        }
      }
      else
      {
        /* Check for menu button press */
        if (y >= (row_height * 9) && x <= 64)
        {
          setScreen(MENU);
        }
        else
        {
          /* Otherwise forward touch to current screen */
          m_screens[m_currentScreenIdx]->handleTouch(x, y);
        }
      }
    }

    void render(bool full)
    {
      device::tft.setTextColor(ILI9341_WHITE, ILI9341_BLACK);
      if (full)
      {
        device::tft.fillScreen(ILI9341_BLACK);
      }

      const bool isMenu(m_currentScreenIdx == MENU);

      if (full)
      {
        /* Render menu title */
        device::tft.setTextSize(2);
        device::tft.setTextColor(ILI9341_CYAN, ILI9341_BLACK);
        device::tft.setCursor(60, (row_height * 9) + 8);
        device::tft.print(isMenu ? "Main Menu" : m_screens[m_currentScreenIdx]->title());
      }

      if (isMenu)
      {
        size_t yOffset(0);
        for (const auto &screen : m_screens)
        {
          device::tft.setTextSize(3);
          device::tft.setCursor(2, yOffset + 4);
          device::tft.print(screen->title());
          device::tft.setCursor(210, yOffset + 4);
          device::tft.setFont(AwesomeF000_18);
          device::tft.drawFontChar(100);
          device::tft.setFontAdafruit();
          yOffset += row_height;
        }
      }
      else
      {
        if (full)
        {
          /* Render back button */
          device::tft.setTextSize(3);
          device::tft.setCursor(2, row_height * 9);
          device::tft.setTextColor(ILI9341_BLUE, ILI9341_BLACK);
          device::tft.setFont(AwesomeF100_18);
          device::tft.drawFontChar(18);
          device::tft.setFontAdafruit();
        }

        m_screens[m_currentScreenIdx]->render(full);
      }
    }

  private:
    Screens m_screens;
    int m_currentScreenIdx;
    uint32_t m_lastScreenRender;
  };
} // namespace display
} // namespace dashboard
