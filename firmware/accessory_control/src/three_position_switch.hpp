#pragma once

class three_position_switch {
public:
  enum class position { Unknown, A, B, C };

public:
  three_position_switch(int const pin_1, int const pin_2);

  void init();
  bool update();

  position pos() const;

private:
  int const m_pin_1;
  int const m_pin_2;

  bool m_pin_1_state;
  bool m_pin_2_state;

  bool m_first_update_done;
};
