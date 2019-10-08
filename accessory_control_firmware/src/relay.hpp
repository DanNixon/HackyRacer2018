#pragma once

class relay {
public:
  relay(int const pin);

  void init();

  void on();
  void off();

private:
  int const m_pin;
};
