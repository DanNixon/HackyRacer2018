#pragma once

#include <vector>

#include "battery_sensor.hpp"
#include "dashboard/value/numeric_units.hpp"

namespace dashboard
{
namespace sensor
{
  class BatteryPackSensor
  {
  public:
    BatteryPackSensor(const std::vector<FrSkySportSensor::SensorId> &sensorIds)
        : cellCount("Cls")
        , totalVoltage("V(pack)")
        , minCellVoltage("V(smin)")
        , maxCellVoltage("V(smax)")
        , cellVoltageDiff("V(diff)")
        , m_batteries()
    {
      minCellVoltage.setLowerThresholds(BatterySensor::lipo_cell_low,
                                        BatterySensor::lipo_cell_critical);
      maxCellVoltage.setLowerThresholds(BatterySensor::lipo_cell_low,
                                        BatterySensor::lipo_cell_critical);
      cellVoltageDiff.setUpperThresholds(0.2f, 0.3f);

      for (const auto &id : sensorIds)
      {
        m_batteries.emplace_back(id);
      }
    }

    void update()
    {
      size_t cells(0);
      float totalVolts(0.0f);
      float minVolts(std::numeric_limits<float>::max());
      float maxVolts(0.0f);

      for (auto &battery : m_batteries)
      {
        battery.update();

        {
          const auto &b(battery);

          cells += b.cellCount.value();
          totalVolts += b.totalVoltage.value();

          if (b.batteryPresent())
          {
            minVolts = std::min(minVolts, b.minCellVoltage.value());
            maxVolts = std::max(maxVolts, b.maxCellVoltage.value());
          }
        }
      }

      if (cells == 0)
      {
        maxVolts = 0.0f;
        minVolts = 0.0f;
      }

      cellCount.setValue(cells);
      totalVoltage.setValue(totalVolts);
      minCellVoltage.setValue(minVolts);
      maxCellVoltage.setValue(maxVolts);
      cellVoltageDiff.setValue(maxVolts - minVolts);
    }

    BatterySensor &battery(const size_t idx)
    {
      return m_batteries[idx];
    }

  public:
    dashboard::value::CellCountValue cellCount;
    dashboard::value::VoltageValue totalVoltage;
    dashboard::value::VoltageValue minCellVoltage;
    dashboard::value::VoltageValue maxCellVoltage;
    dashboard::value::VoltageValue cellVoltageDiff;

  private:
    std::vector<BatterySensor> m_batteries;
  };
}
}
