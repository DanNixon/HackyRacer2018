#pragma once

class pwm_light {
public:
  enum class level { off, medium, full };

public:
  pwm_light(int const pin);

  void init();

  void set(level const l);

private:
  int const m_pin;
};
