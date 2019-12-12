inner_size = [110, 60];
outer_size = inner_size + [10, 10];
centre_section_depth = 30;

corner_radius = 5;

sheet_thickness = 3;

magic_1 = outer_size - [2*corner_radius, 2*corner_radius];

teensy_position = [(outer_size[0] / 2) - 5, -14, 1];
usb_breakout_position = [-outer_size[0] / 2, -15, 0];

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
