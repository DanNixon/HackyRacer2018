#pragma once

#include "numeric.hpp"

namespace dashboard
{
namespace value
{
  class VoltageValue : public NumericValue<float>
  {
  public:
    VoltageValue(const char *name)
        : NumericValue(name, "V")
    {
    }
  };

  class CurrentValue : public NumericValue<float>
  {
  public:
    CurrentValue(const char *name)
        : NumericValue(name, "A")
    {
    }
  };

  class CellCountValue : public NumericValue<unsigned int>
  {
  public:
    CellCountValue(const char *name)
        : NumericValue(name, "S")
    {
    }
  };

  class EnergyValue : public NumericValue<float>
  {
  public:
    EnergyValue(const char *name)
        : NumericValue(name, "Ah")
    {
    }
  };

  class TemperatureValue : public NumericValue<float>
  {
  public:
    TemperatureValue(const char *name)
        : NumericValue(name, "C")
    {
    }
  };

  class RpmValue : public NumericValue<long>
  {
  public:
    RpmValue(const char *name)
        : NumericValue(name, "")
    {
    }
  };

  class DutyCycleValue : public NumericValue<float>
  {
  public:
    DutyCycleValue(const char *name)
        : NumericValue(name, "%")
    {
    }
  };

  class VolumeValue : public NumericValue<float>
  {
  public:
    VolumeValue(const char *name)
        : NumericValue(name, "", 1.0f)
    {
      setWidth(3);
    }
  };
}
}
