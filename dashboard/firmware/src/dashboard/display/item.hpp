#pragma once

namespace dashboard
{
namespace display
{
  class IItem
  {
  public:
    virtual size_t rows() const = 0;
    virtual size_t height() const = 0;

    virtual void render(bool full, int yOffset) const = 0;

    virtual void handleTouch(int x, int y) const {};
  };

  constexpr size_t row_height(32);

  template <size_t HeightInRows> class Item : public IItem
  {
  public:
    size_t rows() const
    {
      return HeightInRows;
    }

    size_t height() const
    {
      return HeightInRows * row_height;
    }
  };
}
}
