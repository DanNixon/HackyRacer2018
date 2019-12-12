use <teensy.scad>
use <usb_breakout.scad>

include <../common.scad>

module Enclosure()
{
  difference()
  {
    linear_extrude(centre_section_depth)
    {
      difference()
      {
        union()
        {
          difference()
          {
            PanelProjectionOuter();
            square(inner_size, center=true);
          }

          /* Assembly screw hole support */
          PlaceAtCentres(magic_1)
          {
            circle(d=10);
          }
        }

        /* Assembly screw holes */
        PlaceAtCentres(magic_1)
        {
          circle(d=3);
        }
      }
    }

    translate(teensy_position)
    {
      Teensy35SdCardCutout();
    }

    translate(usb_breakout_position)
    {
      rotate([0, 0, 180])
      {
        UsbBreakoutCutout();
      }
    }
  }
}

Enclosure();
