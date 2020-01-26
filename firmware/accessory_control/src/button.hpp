#pragma once

class button {
public:
  enum class action { unknown, pressed, released };

public:
  button(int const pin);

  void init();
  bool update();

  action state() const;

private:
  int const m_pin;

  action m_state;
  long int m_last_state_change;
};
