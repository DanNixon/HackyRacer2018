#pragma once

#include "value.hpp"

namespace dashboard
{
namespace value
{
  class BooleanOnlineOfflineValue : public Value<bool>
  {
  public:
    BooleanOnlineOfflineValue(const char *name, const bool initial = false)
        : Value(name, initial)
    {
    }

    virtual std::string to_string() const
    {
      return m_value ? "ONLINE " : "OFFLINE";
    }

  protected:
    virtual IValue::State determineCurrentState() const
    {
      return m_value ? IValue::NORMAL : IValue::CRITICAL;
    }
  };
}
}
