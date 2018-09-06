#pragma once

#include <vector>

#include "item.hpp"

namespace dashboard
{
namespace display
{
  class Screen
  {
  private:
    using Items = std::vector<IItem *>;

  public:
    Screen(const char *title, const Items &items)
        : m_title(title)
        , m_items(items)
    {
    }

    const char *title() const
    {
      return m_title;
    }

    void render(bool full) const
    {
      size_t yOffset(0);
      for (const auto &item : m_items)
      {
        item->render(full, yOffset);
        yOffset += item->height();
      }
    }

    void handleTouch(int x, int y)
    {
      size_t currentY(0);
      for (const auto &item : m_items)
      {
        if (y < (currentY + item->height()))
        {
          /* Fire touch handler with relative Y position */
          item->handleTouch(x, y - currentY);
          return;
        }
        currentY += item->height();
      }
    }

  private:
    const char *m_title;
    Items m_items;
  };
}
}
