use <usb_breakout.scad>

include <../common.scad>

module MountingTab(hole_diameter, hole_centres, outer_radius, lower_offset)
{
  dx = hole_centres / 2;
  magic_1 = 5;

  difference()
  {
    hull()
    {
      square([hole_centres + 2 * outer_radius, magic_1], center=true);

      for(x = [-dx, dx])
      {
        translate([x, magic_1-lower_offset])
        {
          circle(r=outer_radius, $fn=32);
        }
      }
    }

    for(x = [-dx, dx])
    {
      translate([x, magic_1-lower_offset])
      {
        circle(d=hole_diameter, $fn=32);
      }
    }
  }
}

module RearPanel()
{
  difference()
  {
    PanelProjection();

    translate(usb_breakout_position)
    {
      UsbBreakoutHoles();
    }
  }

  translate([0, -outer_size[1] / 2])
  {
    MountingTab(hole_diameter=4.1, hole_centres=50, outer_radius=10, lower_offset=15);
  }
}

RearPanel();
