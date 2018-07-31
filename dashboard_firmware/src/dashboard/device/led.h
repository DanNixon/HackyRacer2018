#pragma once

#define FASTLED_ALLOW_INTERRUPTS 0
#include <FastLED.h>

#include "dashboard/value/enum.hpp"

namespace dashboard
{
namespace device
{
  class LedRange
  {
  public:
    constexpr LedRange(size_t _begin, size_t _end)
        : begin(_begin)
        , end(_end)
    {
    }

    constexpr size_t count() const
    {
      return end - begin;
    }

    const size_t begin;
    const size_t end;
  };

  constexpr LedRange ledsRear(0, 8);
  constexpr LedRange ledsUnder(8, 72);

  constexpr auto ledCount(ledsRear.count() + ledsUnder.count());

  extern CRGB leds[ledCount];

  extern value::EnumValue ledRearMode;
  extern value::EnumValue ledUnderMode;

  enum LedEffect
  {
    LED_OFF,
    LED_WHITE,
    LED_RED,
    LED_GREEN,
    LED_BLUE,
    LED_DISCO
  };

  void ledInit();
  void ledUpdate();
  void ledShow();

  void ledSetRange(const CRGB color, const LedRange &range);
}
}
