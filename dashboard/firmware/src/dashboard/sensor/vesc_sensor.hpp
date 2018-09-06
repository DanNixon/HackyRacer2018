#pragma once

#include <FlexCAN.h>

#include "dashboard/value/boolean.hpp"
#include "dashboard/value/numeric_units.hpp"

namespace dashboard
{
namespace sensor
{
  class VescSensor
  {
  public:
    static constexpr uint32_t STATUS_ID = 9 << 8;

  public:
    VescSensor(const uint32_t canId)
        : m_canId(canId)
        , online("Comm")
        , rpm("RPM")
        , current("I(mtr)")
        , dutyCycle("Duty")
    {
      dutyCycle.setPrecision(3);
      current.setUpperThresholds(30.0f, 45.0f);
    }

    void update()
    {
      static constexpr auto timeout(500);

      if (millis() - m_lastMessageTime > timeout)
      {
        online.setValue(false);
      }
    }

    bool processCanMessage(const CAN_message_t &msg)
    {
      if (msg.ext != 1 || msg.id != (m_canId | STATUS_ID))
      {
        return false;
      }

      bool result(false);

      /* The standard VESC CAN status message */
      if (msg.len == 8)
      {
        const uint8_t *b(msg.buf);

        rpm.setValue((int32_t)(b[0] << 24 | b[1] << 16 | b[2] << 8 | b[3]));
        current.setValue((int16_t)(b[4] << 8 | b[5]) / 10.0f);
        dutyCycle.setValue((int16_t)(b[6] << 8 | b[7]) / 1000.0f);

        result = true;
      }

      /* Record good RX */
      if (result)
      {
        online.setValue(true);
        m_lastMessageTime = millis();
      }

      return result;
    }

  private:
    const uint32_t m_canId;

    uint32_t m_lastMessageTime;

  public:
    dashboard::value::BooleanOnlineOfflineValue online;
    dashboard::value::RpmValue rpm;
    dashboard::value::CurrentValue current;
    dashboard::value::DutyCycleValue dutyCycle;
  };
}
}
