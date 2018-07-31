#pragma once

#include <cmath>
#include <limits>

#include <FrSkySportSensorFlvss.h>

#include "dashboard/value/numeric_units.hpp"

namespace dashboard
{
namespace sensor
{
  class BatterySensor
  {
  public:
    static constexpr float lipo_cell_low = 3.5f;
    static constexpr float lipo_cell_critical = 3.3f;

  public:
    BatterySensor(FrSkySportSensor::SensorId id)
        : cellCount("Cls")
        , totalVoltage("V(batt)")
        , minCellVoltage("V(smin)")
        , maxCellVoltage("V(smax)")
        , cellVoltage1("V(s1)")
        , cellVoltage2("V(s2)")
        , cellVoltage3("V(s3)")
        , cellVoltage4("V(s4)")
        , cellVoltage5("V(s5)")
        , cellVoltage6("V(s6)")
        , m_flvss(id)
    {
      minCellVoltage.setLowerThresholds(lipo_cell_low, lipo_cell_critical);
      maxCellVoltage.setLowerThresholds(lipo_cell_low, lipo_cell_critical);

      cellVoltage1.setLowerThresholds(lipo_cell_low, lipo_cell_critical);
      cellVoltage2.setLowerThresholds(lipo_cell_low, lipo_cell_critical);
      cellVoltage3.setLowerThresholds(lipo_cell_low, lipo_cell_critical);
      cellVoltage4.setLowerThresholds(lipo_cell_low, lipo_cell_critical);
      cellVoltage5.setLowerThresholds(lipo_cell_low, lipo_cell_critical);
      cellVoltage6.setLowerThresholds(lipo_cell_low, lipo_cell_critical);
    }

    void update()
    {
      size_t cells(0);
      float totalVolts(0.0f);
      float minCellVolts(std::numeric_limits<float>::max());
      float maxCellVolts(0.0f);

#define RECORD_CELL_VOLTAGE(sensor, flvss_sensor)                                                  \
  {                                                                                                \
    const auto cellVolts = m_flvss.flvss_sensor();                                                 \
    sensor.setValue(cellVolts);                                                                    \
    const bool validCell(!std::isnan(cellVolts) && !std::isinf(cellVolts) && cellVolts >= 0.5f);   \
    cells += validCell ? 1 : 0;                                                                    \
    totalVolts += cellVolts;                                                                       \
    if (validCell)                                                                                 \
    {                                                                                              \
      minCellVolts = std::min(minCellVolts, cellVolts);                                            \
      maxCellVolts = std::max(maxCellVolts, cellVolts);                                            \
    }                                                                                              \
  }

      RECORD_CELL_VOLTAGE(cellVoltage1, getCell1);
      RECORD_CELL_VOLTAGE(cellVoltage2, getCell2);
      RECORD_CELL_VOLTAGE(cellVoltage3, getCell3);
      RECORD_CELL_VOLTAGE(cellVoltage4, getCell4);
      RECORD_CELL_VOLTAGE(cellVoltage5, getCell5);
      RECORD_CELL_VOLTAGE(cellVoltage6, getCell6);

#undef RECORD_CELL_VOLTAGE

      cellCount.setValue(cells);
      totalVoltage.setValue(totalVolts);

      if (cells == 0)
      {
        minCellVolts = 0.0f;
        maxCellVolts = 0.0f;
      }

      minCellVoltage.setValue(minCellVolts);
      maxCellVoltage.setValue(maxCellVolts);
    }

    bool batteryPresent() const
    {
      return cellCount.value() > 0;
    }

    FrSkySportSensorFlvss *flvssPtr()
    {
      return &m_flvss;
    }

  public:
    dashboard::value::CellCountValue cellCount;
    dashboard::value::VoltageValue totalVoltage;
    dashboard::value::VoltageValue minCellVoltage;
    dashboard::value::VoltageValue maxCellVoltage;
    dashboard::value::VoltageValue cellVoltage1;
    dashboard::value::VoltageValue cellVoltage2;
    dashboard::value::VoltageValue cellVoltage3;
    dashboard::value::VoltageValue cellVoltage4;
    dashboard::value::VoltageValue cellVoltage5;
    dashboard::value::VoltageValue cellVoltage6;

  private:
    FrSkySportSensorFlvss m_flvss;
  };
}
}
