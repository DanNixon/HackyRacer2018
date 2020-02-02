#pragma once

namespace device {
class relay {
public:
  relay(int const pin);

  void init();

  void on();
  void off();

private:
  int const m_pin;
};
} // namespace device
