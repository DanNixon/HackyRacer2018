include <../common.scad>

module DisplayMountingHoles()
{
  PlaceAtCentres([76, 44.5])
  {
    circle(d=3.2, $fn=32);
  }
}

module FrontPanel()
{
  difference()
  {
    PanelProjection();
    DisplayMountingHoles();
  }
}

FrontPanel();
