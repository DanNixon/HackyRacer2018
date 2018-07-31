#pragma once

#include <limits>
#include <string>

namespace dashboard
{
namespace value
{
  class IValue
  {
  public:
    enum State
    {
      NORMAL,
      WARN,
      CRITICAL
    };

    enum DirtyBit
    {
      DIRTY_DEBUG = (1 << 0),
      DIRTY_DISPLAY = (1 << 1),
      DIRTY_ANNOUNCE = (1 << 2),
      DIRTY_PARAMETER = (1 << 3),
      DIRTY_USER1 = (1 << 4),
      DIRTY_USER2 = (1 << 5),
      DIRTY_USER3 = (1 << 6),
      DIRTY_USER4 = (1 << 7),
    };

  public:
    IValue(const char *name)
        : m_name(name)
        , m_state(NORMAL)
        , m_valueDirty(0xFF)
        , m_stateDirty(0xFF)
    {
    }

    const char *name() const
    {
      return m_name;
    }

    State state() const
    {
      return m_state;
    }

    bool valueDirty(const uint8_t flag, const bool reset) const
    {
      const bool isDirtyForFlag(m_valueDirty & flag);
      if (reset)
      {
        m_valueDirty &= ~flag;
      }
      return isDirtyForFlag;
    }

    bool stateDirty(const uint8_t flag, const bool reset) const
    {
      const bool isDirtyForFlag(m_stateDirty & flag);
      if (reset)
      {
        m_stateDirty &= ~flag;
      }
      return isDirtyForFlag;
    }

  public:
    virtual std::string to_string() const = 0;

  protected:
    virtual State determineCurrentState() const
    {
      return NORMAL;
    }

  protected:
    const char *m_name;
    State m_state;
    mutable uint8_t m_valueDirty;
    mutable uint8_t m_stateDirty;
  };

  template <typename T> class Value : public IValue
  {
  public:
    Value(const char *name, const T initial = T())
        : IValue(name)
    {
      setValue(initial);
    }

    const T value() const
    {
      return m_value;
    }

    virtual void setValue(const T value)
    {
      /* If values differ then set dirty flags */
      if (value != m_value)
      {
        m_valueDirty = 0xFF;
      }

      /* Record value */
      m_value = value;

      /* Determine new state */
      const auto newState(determineCurrentState());

      /* If states differ then set dirty flags */
      if (newState != m_state)
      {
        m_stateDirty = 0xFF;
      }

      /* Record new state */
      m_state = newState;
    }

    virtual std::string to_string() const = 0;

  protected:
    T m_value;
  };
}
}
