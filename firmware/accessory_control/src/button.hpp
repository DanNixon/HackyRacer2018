#pragma once

class button {
public:
  enum class action { unknown, pressed, released_short, released_long };

public:
  button(int const pin, unsigned long const long_press_time_ms = 1500);

  void init();
  bool update();

  action state() const;

private:
  int const m_pin;
  unsigned long const m_long_press_time_ms;

  action m_state;
  long int m_last_state_change;
};
