module ScreenCutaway(
    board_size=[52, 90],
    screen_extents=20,
    hole_diameter=3.5,
    hole_extents=20)
{
  board_thickness = 2.5;

  display_size = [52, 72];
  display_thickness = 4;
  display_offset = [0, 3];

  screen_size = [45, 60];
  screen_offset = [0, 5];

  hole_centres = [44, 76];
  hole_offset = [0, 3];

  bottom_pin_header_size = [40, 4];
  bottom_pin_header_height = 2;
  bottom_pin_header_offset = [0, -40];

  module Extrusion(pos, size, height)
  {
    linear_extrude(height)
    {
      translate(pos)
      {
        square(size, center=true);
      }
    }
  }

  color("red")
  {
    Extrusion([0, 0], board_size, board_thickness);
  }

  color("silver")
  {
    Extrusion(display_offset, display_size, board_thickness + display_thickness);
  }

  color("green")
  {
    Extrusion(screen_offset, screen_size, screen_extents);
  }

  color("cyan")
  {
    Extrusion(bottom_pin_header_offset, bottom_pin_header_size, board_thickness + bottom_pin_header_height);
  }

  translate(hole_offset)
  {
    dd = hole_centres / 2;
    for(x=[-dd[0], dd[0]])
    {
      for(y=[-dd[1], dd[1]])
      {
        translate([x, y])
        {
          color("green")
          {
            cylinder(d=hole_diameter, h=hole_extents, $fn=64);
          }
        }
      }
    }
  }
}
