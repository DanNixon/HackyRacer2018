use <clamp.scad>
use <common.scad>
use <plate_3d.scad>
use <vesc.scad>
include <config.scad>

color("silver")
{
  Plate3D();
}

color("red")
{
  PlaceAtCentres(plate_mounting_hole_centres)
  {
    Clamp();
  }
}

color("black")
{
  VESC();
}
