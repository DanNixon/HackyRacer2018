#include <gtest/gtest.h>

#include "dashboard/value/boolean.hpp"
#include "dashboard/value/enum.hpp"
#include "dashboard/value/numeric.hpp"
#include "dashboard/value/numeric_units.hpp"
#include "dashboard/value/value.hpp"

TEST(ValueTest, test_dirty)
{
  dashboard::value::VoltageValue volts("volts");

  for (auto i = 1; i < 8; i++)
  {
    EXPECT_TRUE(volts.valueDirty((1 << i), false));
  }

  for (auto i = 1; i < 8; i++)
  {
    EXPECT_TRUE(volts.valueDirty((1 << i), true));
  }

  for (auto i = 1; i < 8; i++)
  {
    EXPECT_FALSE(volts.valueDirty((1 << i), false));
  }

  EXPECT_TRUE(volts.valueDirty(dashboard::value::IValue::DIRTY_DEBUG, true));

  EXPECT_FALSE(volts.valueDirty(dashboard::value::IValue::DIRTY_DEBUG, true));

  volts.setValue(45.0f);

  for (auto i = 0; i < 8; i++)
  {
    EXPECT_TRUE(volts.valueDirty((1 << i), false));
  }
}
