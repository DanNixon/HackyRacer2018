#include <FlexCAN.h>
#include <FrSkySportDecoder.h>
#include <FrSkySportSensor.h>
#include <SD.h>

#include "dashboard/device/audio.h"
#include "dashboard/device/horn.h"
#include "dashboard/device/tft.h"
#include "dashboard/device/touchscreen.h"
#include "dashboard/display/item_double_height_value.hpp"
#include "dashboard/display/item_enum_param.hpp"
#include "dashboard/display/item_label.hpp"
#include "dashboard/display/item_music_control.hpp"
#include "dashboard/display/item_single_height_value.hpp"
#include "dashboard/display/item_volume_control.hpp"
#include "dashboard/display/menu.hpp"
#include "dashboard/display/screen.hpp"
#include "dashboard/sensor/battery_pack_sensor.hpp"
#include "dashboard/sensor/vesc_sensor.hpp"
#include "pin_config.h"

#include "dashboard/device/led.h"

using namespace dashboard;

sensor::BatteryPackSensor batteryPack({FrSkySportSensor::ID2, FrSkySportSensor::ID3});
FrSkySportDecoder sportDecoder(true);

FlexCAN canBus(CAN_BAUD, CAN_DEVICE);
sensor::VescSensor vesc(VESC_CAN_ID);

display::SingleHeightValueItem itemVescCurrent(&vesc.current);
display::SingleHeightValueItem itemVescDutyCycle(&vesc.dutyCycle);
display::SingleHeightValueItem itemVescRpm(&vesc.rpm);
display::SingleHeightValueItem itemVescOnline(&vesc.online);
display::Screen screenVesc("VESC",
                           {&itemVescCurrent, &itemVescDutyCycle, &itemVescRpm, &itemVescOnline});

display::SingleHeightValueItem itemPackVoltage(&batteryPack.totalVoltage);
display::SingleHeightValueItem itemPackCellCount(&batteryPack.cellCount);
display::SingleHeightValueItem itemPackMinCellVoltage(&batteryPack.minCellVoltage);
display::SingleHeightValueItem itemPackMaxCellVoltage(&batteryPack.maxCellVoltage);
display::SingleHeightValueItem itemPackCellVoltageDiff(&batteryPack.cellVoltageDiff);
display::Screen screenBatteryPack("Batt Pack",
                                  {&itemPackVoltage, &itemPackCellCount, &itemPackMinCellVoltage,
                                   &itemPackMaxCellVoltage, &itemPackCellVoltageDiff});

display::SingleHeightValueItem itemBattery1Voltage(&batteryPack.battery(0).totalVoltage);
display::SingleHeightValueItem itemBattery1CellCount(&batteryPack.battery(0).cellCount);
display::SingleHeightValueItem itemBattery1Cell1(&batteryPack.battery(0).cellVoltage1);
display::SingleHeightValueItem itemBattery1Cell2(&batteryPack.battery(0).cellVoltage2);
display::SingleHeightValueItem itemBattery1Cell3(&batteryPack.battery(0).cellVoltage3);
display::SingleHeightValueItem itemBattery1Cell4(&batteryPack.battery(0).cellVoltage4);
display::SingleHeightValueItem itemBattery1Cell5(&batteryPack.battery(0).cellVoltage5);
display::SingleHeightValueItem itemBattery1Cell6(&batteryPack.battery(0).cellVoltage6);
display::Screen screenBattery1("Battery 1",
                               {&itemBattery1Voltage, &itemBattery1CellCount, &itemBattery1Cell1,
                                &itemBattery1Cell2, &itemBattery1Cell3, &itemBattery1Cell4,
                                &itemBattery1Cell5, &itemBattery1Cell6});

display::SingleHeightValueItem itemBattery2Voltage(&batteryPack.battery(1).totalVoltage);
display::SingleHeightValueItem itemBattery2CellCount(&batteryPack.battery(1).cellCount);
display::SingleHeightValueItem itemBattery2Cell1(&batteryPack.battery(1).cellVoltage1);
display::SingleHeightValueItem itemBattery2Cell2(&batteryPack.battery(1).cellVoltage2);
display::SingleHeightValueItem itemBattery2Cell3(&batteryPack.battery(1).cellVoltage3);
display::SingleHeightValueItem itemBattery2Cell4(&batteryPack.battery(1).cellVoltage4);
display::SingleHeightValueItem itemBattery2Cell5(&batteryPack.battery(1).cellVoltage5);
display::SingleHeightValueItem itemBattery2Cell6(&batteryPack.battery(1).cellVoltage6);
display::Screen screenBattery2("Battery 2",
                               {&itemBattery2Voltage, &itemBattery2CellCount, &itemBattery2Cell1,
                                &itemBattery2Cell2, &itemBattery2Cell3, &itemBattery2Cell4,
                                &itemBattery2Cell5, &itemBattery2Cell6});

display::LabelItem itemMusicNowPlaying("Now Playing", 2);
display::MusicControlItem itemMusicControls;
display::VolumeControlItem itemMusicVolume(&device::audioMusicVolume);
display::VolumeControlItem itemHornVolume(&device::audioHornVolume);
display::EnumParameterItem itemRearLed(&device::ledRearMode);
display::EnumParameterItem itemLowerLed(&device::ledUnderMode);
display::Screen screenAccessory("Accessory",
                                {&itemMusicNowPlaying, &itemMusicControls, &itemMusicVolume,
                                 &itemHornVolume, &itemRearLed, &itemLowerLed});

display::DoubleHeightValueItem itemMainVescCurrent(&vesc.current);
display::DoubleHeightValueItem itemMainPackVoltage(&batteryPack.totalVoltage);
display::DoubleHeightValueItem itemMainPackMinCellVoltage(&batteryPack.minCellVoltage);
display::Screen screenMainDash("Main", {&itemMainVescCurrent, &itemMainPackVoltage,
                                        &itemMainPackMinCellVoltage, &itemPackCellVoltageDiff});

display::Menu menu({&screenMainDash, &screenVesc, &screenBatteryPack, &screenBattery1,
                    &screenBattery2, &screenAccessory});

void setup()
{
  Serial.begin(9600);
  /* while (!Serial) */
  {
  }
  Serial.println("Hello");

  /* SD card */
  const bool sdCardOk(SD.begin(BUILTIN_SDCARD));
  Serial.print("SD card OK: ");
  Serial.println(sdCardOk);

  /* Audio */
  device::audioInit();

  /* TFT display */
  device::tftInit();

  /* Touchscreen */
  device::touchscreenInit();

  /* Horn (switch + audio) */
  device::hornInit();

  /* S.PORT decoder */
  sportDecoder.begin(SPORT_SERIAL, batteryPack.battery(0).flvssPtr(),
                     batteryPack.battery(1).flvssPtr());

  /* CAN bus */
  canBus.begin();

  /* LEDs init */
  device::ledInit();

  /* Initial menu render */
  menu.init();
}

void loop(void)
{
  /* Handle menu update */
  menu.update();

  /* Audio update */
  device::audioUpdate();
  itemMusicNowPlaying.setText(device::audioMusicFiles()[device::audioMusicNowPlaying()]);

  /* Horn update */
  device::hornUpdate();

  /* VESC sensor update */
  if (canBus.available())
  {
    CAN_message_t msg;
    while (canBus.read(msg))
    {
      vesc.processCanMessage(msg);
    }
  }
  vesc.update();

  /* S.PORT sensors update */
  sportDecoder.decode();
  batteryPack.update();

  /* LED update */
  device::ledUpdate();
}
