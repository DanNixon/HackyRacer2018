use <common.scad>
use <components.scad>
include <config.scad>

module CaseLower(show_parts=false)
{
  difference()
  {
    union()
    {
      /* Panel */
      linear_extrude(panel_thickness)
      {
        PointHull([p_ulo, p_uro, p_llo, p_lro]);
      }

      /* Screw mounts */
      for(p=p_screws)
      {
        translate(p)
        {
          cylinder(h=panel_thickness+outer_bar_diameter, d=mount_screw_outer, $fn=32);
        }
      }

      translate([0, 0, panel_thickness])
      {
        /* Walls */
        linear_extrude(outer_bar_diameter)
        {
          PointHull([p_ulo, p_llo]);
          PointHull([p_uli, p_lli]);

          PointHull([p_uml, p_lml]);
          PointHull([p_umr, p_lmr]);

          PointHull([p_uri, p_lri]);
          PointHull([p_uro, p_lro]);

          PointHull([p_uli, p_uml]);
          PointHull([p_umr, p_uri]);

          PointHull([p_lli, p_lml]);
          PointHull([p_lmr, p_lri]);
        }

        translate(can_board_position)
        {
          if(show_parts)
          {
            CanTranscieverBoard();
          }

          PlaceCanTranscieverBoardHoles()
          {
            cylinder(h=3, d=5, $fn=16);
          }
        }

        translate(amplifier_board_pos)
        {
          rotate([0, 0, -90])
          {
            if(show_parts)
            {
              AmplifierBoard();
            }

            PlaceAmplifierBoardHoles()
            {
              cylinder(h=3, d=5, $fn=16);
            }
          }
        }

        if(show_parts)
        {
          translate(usb_board_pos)
          {
            UsbBoard();
          }

          translate(teensy_board_pos)
          {
            Teensy35Board();
          }

          translate(bec_module_pos)
          {
            BecModule();
          }
        }
      }
    }

    translate([0, 0, -1])
    {
      translate(usb_board_pos)
      {
        PlaceUsbBoardHoles()
        {
          cylinder(h=10, d=3.5, $fn=16);
        }
      }
    }

    translate([0, 0, 0.25])
    {
      translate(can_board_position)
      {
        PlaceCanTranscieverBoardHoles()
        {
          cylinder(h=10, d=small_screw_diameter, $fn=16);
        }
      }

      translate(amplifier_board_pos)
      {
        rotate([0, 0, -90])
        {
          PlaceAmplifierBoardHoles()
          {
            cylinder(h=10, d=small_screw_diameter, $fn=16);
          }
        }
      }
    }

    translate([0, 0, -1])
    {
      translate(bec_module_pos)
      {
        PlaceBecModuleHoles()
        {
          cylinder(h=10, d=3, $fn=16);
        }
      }
    }

    /* Enclosure mounting screws */
    translate([0, 0, panel_thickness+outer_bar_diameter+0.1])
    {
      for(p=p_screws)
      {
        translate(p)
        {
          rotate([180, 0, 0])
          {
            cylinder(h=15, d=mount_screw_diameter, $fn=32);
          }
        }
      }
    }

    /* SD card slot */
    translate([-19, -40, 8])
    {
      cube([18, 10, 8], center=true);
    }

    /* USB port */
    translate([usb_board_pos[0], 42, panel_thickness+3])
    {
      cube([14, 10, 6], center=true);
    }

    /* Power in wiring */
    translate([bec_module_pos[0], -42, 22])
    {
      cube([5, 5, 5], center=true);
    }

    /* Power out wiring */
    translate([bec_module_pos[0], 42, 22])
    {
      cube([5, 5, 5], center=true);
    }

    /* Power through wiring */
    translate([0, 34, 22])
    {
      cube([25, 5, 5], center=true);
    }

    /* Data cable wiring */
    translate([-38, 42, 20])
    {
      cube([5, 10, 10], center=true);
    }
  }
}

CaseLower(show_parts=false);
