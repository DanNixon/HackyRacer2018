#pragma once

namespace device {
class pwm_light {
public:
  enum class level { off, low, high, on };

public:
  pwm_light(int const pin, int const on_level);
  pwm_light(int const pin, int const low_level, int const high_level);

  void init();

  void on();
  void off();

  void set(level const l);

private:
  int const m_pin;

  int const m_low_level;
  int const m_high_level;
};
} // namespace device
