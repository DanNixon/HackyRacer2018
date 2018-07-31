#pragma once

#include <string>
#include <vector>

#include "value.hpp"

namespace dashboard
{
namespace value
{
  class EnumValue : public Value<size_t>
  {
  public:
    using NamesType = std::vector<std::string>;

  public:
    EnumValue(const char *name, const size_t initial, const NamesType &valueNames)
        : Value(name, initial)
        , m_valueNames(valueNames)
    {
    }

    size_t stateCount() const
    {
      return m_valueNames.size();
    }

    void advanceToNextState()
    {
      auto next(m_value + 1);
      if (next >= stateCount())
      {
        next = 0;
      }
      setValue(next);
    }

    virtual std::string to_string() const
    {
      return m_valueNames[m_value];
    }

  private:
    const NamesType m_valueNames;
  };
}
}
