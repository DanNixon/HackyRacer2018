include <../common.scad>

module Enclosure()
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
}

Enclosure();
