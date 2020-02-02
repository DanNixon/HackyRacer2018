#pragma once

#include <bitset>
#include <functional>

namespace value {
enum class State {
  normal,
  warning,
  critical,
};

enum class DirtyBit {
  display,
  data_logger,
  user_1,
  user_2,
  user_3,
  user_4,
  user_5,
  user_6,
};

template <typename T> using StateUpdateFn = std::function<State(T const &v)>;

class IValue {
public:
  IValue(std::string const &name)
      : m_name(name) {
  }

  std::string name() const {
    return m_name;
  }

  State state() const {
    return m_state;
  }

  bool is_dirty(DirtyBit const bit) const {
    return m_dirty.test(static_cast<int>(bit));
  }

private:
  std::string const m_name;

protected:
  State m_state;
  std::bitset<8> m_dirty;
};

template <typename T> class Value : public IValue {
public:
  Value(
      std::string const &name, StateUpdateFn<T> const &state_update_fn =
                                   [](T const &) { return State::normal; })
      : IValue(name)
      , m_state_update_fn(state_update_fn) {
    set(T());
  }

  void set(T const &v) {
    for (int i = 0; i < m_dirty.size(); ++i)
      m_dirty.set(i);
    m_value = v;
    m_state = m_state_update_fn(v);
  }

  T get(DirtyBit const bit) {
    m_dirty.reset(static_cast<int>(bit));
    return m_value;
  }

private:
  StateUpdateFn<T> const m_state_update_fn;
  T m_value;
};

template <typename T> class NumericValue : public Value<T> {
public:
  NumericValue(
      std::string const &name, std::string const &unit,
      StateUpdateFn<T> const &state_update_fn =
          [](T const &) { return State::normal; })
      : Value<T>(name, state_update_fn)
      , m_unit(unit) {
  }

  std::string unit() const {
    return m_unit;
  }

private:
  std::string const m_unit;
};
} // namespace value
