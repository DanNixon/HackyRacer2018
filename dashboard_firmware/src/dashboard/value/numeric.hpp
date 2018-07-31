#pragma once

#include <iomanip>
#include <sstream>

#include "value.hpp"

namespace dashboard
{
namespace value
{
  template <typename T> class NumericValue : public Value<T>
  {
  public:
    NumericValue(const char *name, const char *unitSymbol, const T initial = T())
        : Value<T>(name, initial)
        , m_unitSymbol(unitSymbol)
        , m_width(6)
        , m_precision(2)
        , m_warnLower(std::numeric_limits<T>::lowest())
        , m_criticalLower(std::numeric_limits<T>::lowest())
        , m_warnUpper(std::numeric_limits<T>::max())
        , m_criticalUpper(std::numeric_limits<T>::max())
    {
    }

    void setWidth(unsigned int width)
    {
      m_width = width;
    }

    void setPrecision(unsigned int precision)
    {
      m_precision = precision;
    }

    void setLowerThresholds(const T warn, const T critical)
    {
      m_warnLower = warn;
      m_criticalLower = critical;

      if (m_criticalLower > m_warnLower)
      {
        std::swap(m_warnLower, m_criticalLower);
      }
    }

    void setUpperThresholds(const T warn, const T critical)
    {
      m_warnUpper = warn;
      m_criticalUpper = critical;

      if (m_criticalUpper < m_warnUpper)
      {
        std::swap(m_warnUpper, m_criticalUpper);
      }
    }

    virtual std::string to_string() const
    {
      std::stringstream str;
      str << std::setw(m_width) << std::fixed << std::setprecision(m_precision) << this->m_value
          << m_unitSymbol;
      return str.str();
    };

  protected:
    virtual IValue::State determineCurrentState() const
    {
      auto state(IValue::NORMAL);
      if (this->m_value <= m_criticalLower || this->m_value >= m_criticalUpper)
      {
        state = IValue::CRITICAL;
      }
      else if (this->m_value <= m_warnLower || this->m_value >= m_warnUpper)
      {
        state = IValue::WARN;
      }
      return state;
    }

  private:
    const char *m_unitSymbol;

    unsigned int m_width;
    unsigned int m_precision;

    T m_warnLower;
    T m_criticalLower;
    T m_warnUpper;
    T m_criticalUpper;
  };
}
}
