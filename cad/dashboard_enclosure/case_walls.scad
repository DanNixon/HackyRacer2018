use <common.scad>
include <config.scad>

module CaseWalls(h)
{
  difference()
  {
    union()
    {
      linear_extrude(height=h)
      {
        PointHull([p_ulo, p_uli, p_lli, p_llo]);
        PointHull([p_uro, p_uri, p_lri, p_lro]);

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

      /* Screw mounts */
      for(p=p_screws)
      {
        translate(p)
        {
          cylinder(h=h, d=mount_screw_outer, $fn=32);
        }
      }
    }

    /* Enclosure mounting screws */
    translate([0, 0, -1])
    {
      for(p=p_screws)
      {
        translate(p)
        {
          cylinder(h=h+2, d=upper_mount_screw_diameter, $fn=32);
        }
      }
    }
  }
}

CaseWalls(4);
