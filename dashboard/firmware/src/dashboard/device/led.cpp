#include "led.h"

#include <string>
#include <vector>

#include "pin_config.h"

namespace dashboard
{
namespace device
{
  const value::EnumValue::NamesType ledEffectNames{
      "Off", "White", "Red", "Green", "Blue", "Cyan", "Magenta", "Yellow", "Disco", "Disco Fast"};

  CRGB leds[ledCount];
  value::EnumValue ledRearMode("Rear", LED_RED, ledEffectNames);
  value::EnumValue ledUnderMode("Under", LED_BLUE, ledEffectNames);

  void ledEffectEnter(const LedRange &range, LedEffect effect);
  void ledEffectOperate(const LedRange &range, LedEffect effect, uint32_t now);

  void ledInit()
  {
    FastLED.addLeds<NEOPIXEL, LED_DATA_PIN>(leds, ledCount);
  }

  void ledUpdate()
  {
    /* Watch for effect changes */
    if (ledRearMode.valueDirty(value::IValue::DIRTY_PARAMETER, true))
    {
      ledEffectEnter(ledsRear, (LedEffect)ledRearMode.value());
      ledShow();
    }
    if (ledUnderMode.valueDirty(value::IValue::DIRTY_PARAMETER, true))
    {
      ledEffectEnter(ledsUnder, (LedEffect)ledUnderMode.value());
      ledShow();
    }

    /* Handle operating current effect */
    static uint32_t lastOperateTime(0);
    const auto now(millis());
    if (now - lastOperateTime > 50)
    {
      ledEffectOperate(ledsRear, (LedEffect)ledRearMode.value(), now);
      ledEffectOperate(ledsUnder, (LedEffect)ledUnderMode.value(), now);
      lastOperateTime = now;
    }
  }

  void ledShow()
  {
    FastLED.show();
  }

  void ledSetRange(const CRGB color, const LedRange &range)
  {
    for (size_t i = range.begin; i < range.end; i++)
    {
      device::leds[i] = color;
    }
  }

  void ledEffectEnter(const LedRange &range, LedEffect effect)
  {
    switch (effect)
    {
    case LED_OFF:
      ledSetRange(CRGB::Black, range);
      break;
    case LED_WHITE:
      ledSetRange(CRGB::White, range);
      break;
    case LED_RED:
      ledSetRange(CRGB::Red, range);
      break;
    case LED_GREEN:
      ledSetRange(CRGB::Green, range);
      break;
    case LED_BLUE:
      ledSetRange(CRGB::Blue, range);
      break;
    case LED_CYAN:
      ledSetRange(CRGB::Cyan, range);
      break;
    case LED_MAGENTA:
      ledSetRange(CRGB::Magenta, range);
      break;
    case LED_YELLOW:
      ledSetRange(CRGB::Yellow, range);
      break;
    default:
      break;
    }
  }

  void ledEffectOperate(const LedRange &range, LedEffect effect, uint32_t now)
  {
    switch (effect)
    {
    case LED_DISCO:
    case LED_DISCO_FAST:
    {
      static uint32_t lastOperateTime(0);
      static unsigned int stage(0);
      const auto timeout(effect == LED_DISCO_FAST ? 200 : 400);
      if (now - lastOperateTime > timeout)
      {
        switch (stage)
        {
        case 0:
          ledSetRange(CRGB::Red, range);
          break;
        case 1:
          ledSetRange(CRGB::Green, range);
          break;
        case 2:
          ledSetRange(CRGB::Blue, range);
          break;
        case 3:
          ledSetRange(CRGB::Cyan, range);
          break;
        case 4:
          ledSetRange(CRGB::Magenta, range);
          break;
        case 5:
          ledSetRange(CRGB::Yellow, range);
          break;
        case 6:
          ledSetRange(CRGB::White, range);
          break;
        default:
          break;
        }
        stage = (stage + 1) % 7;
        ledShow();
        lastOperateTime = now;
      }
      break;
    }
    default:
      break;
    }
  }
}
}
