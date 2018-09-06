#include <gtest/gtest.h>

#include "dashboard/value/numeric_units.hpp"

using namespace dashboard::value;

TEST(NumericValueTest, test_dirty)
{
  VoltageValue minCellVoltage("V(smin)");
  minCellVoltage.setLowerThresholds(3.5f, 3.3f);

  minCellVoltage.setValue(4.2f);
  EXPECT_TRUE(minCellVoltage.valueDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_FLOAT_EQ(4.2f, minCellVoltage.value());
  EXPECT_TRUE(minCellVoltage.stateDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_EQ(IValue::NORMAL, minCellVoltage.state());

  minCellVoltage.setValue(4.0f);
  EXPECT_TRUE(minCellVoltage.valueDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_FLOAT_EQ(4.0f, minCellVoltage.value());
  EXPECT_FALSE(minCellVoltage.stateDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_EQ(IValue::NORMAL, minCellVoltage.state());

  minCellVoltage.setValue(3.5f);
  EXPECT_TRUE(minCellVoltage.valueDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_FLOAT_EQ(3.5f, minCellVoltage.value());
  EXPECT_TRUE(minCellVoltage.stateDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_EQ(IValue::WARN, minCellVoltage.state());

  minCellVoltage.setValue(3.3f);
  EXPECT_TRUE(minCellVoltage.valueDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_FLOAT_EQ(3.3f, minCellVoltage.value());
  EXPECT_TRUE(minCellVoltage.stateDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_EQ(IValue::CRITICAL, minCellVoltage.state());

  minCellVoltage.setValue(3.8f);
  EXPECT_TRUE(minCellVoltage.valueDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_FLOAT_EQ(3.8f, minCellVoltage.value());
  EXPECT_TRUE(minCellVoltage.stateDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_EQ(IValue::NORMAL, minCellVoltage.state());

  minCellVoltage.setValue(3.8f);
  EXPECT_FALSE(minCellVoltage.valueDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_FLOAT_EQ(3.8f, minCellVoltage.value());
  EXPECT_FALSE(minCellVoltage.stateDirty(IValue::DIRTY_DEBUG, true));
  EXPECT_EQ(IValue::NORMAL, minCellVoltage.state());
}
