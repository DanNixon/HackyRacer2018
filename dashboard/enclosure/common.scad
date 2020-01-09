inner_size = [90, 65];
outer_size = inner_size + [7, 7];
centre_section_depth = 35;

display_offset = [-2, 0];

corner_radius = 5;

sheet_thickness = 3;

magic_1 = outer_size - [2 * corner_radius, 2 * corner_radius];

teensy_position = [(outer_size[0] / 2) - 5, -15, 2];
usb_breakout_position = [-outer_size[0] / 2, -16, 0];

cable_entry_position = [(-outer_size[0] / 2) + 8, 0, 0];

module PlaceAtCentres(c)
{
  d = c / 2;
  for(x = [-d[0], d[0]])
  {
    for(y = [-d[1], d[1]])
    {
      translate([x, y])
      {
        children();
      }
    }
  }
}

module PanelProjectionOuter()
{
  minkowski()
  {
    square(magic_1, center=true);
    circle(r=corner_radius);
  }
}

module AssemblyHolesProjection(d)
{
  PlaceAtCentres(magic_1)
  {
    circle(d=d, $fn=32);
  }
}

module PanelProjection()
{

  difference()
  {
    PanelProjectionOuter();
    AssemblyHolesProjection(3.1);
  }
}

module MountingTab(hole_diameter, hole_centres, outer_radius, hole_offset)
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
        translate([x, hole_offset])
        {
          circle(r=outer_radius, $fn=32);
        }
      }
    }

    for(x = [-dx, dx])
    {
      translate([x, hole_offset])
      {
        circle(d=hole_diameter, $fn=32);
      }
    }
  }
}
