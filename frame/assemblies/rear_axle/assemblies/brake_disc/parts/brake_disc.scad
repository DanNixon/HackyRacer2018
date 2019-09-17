module BrakeDisc()
{
  $fn = 64;

  color("magenta")
  {
    /* TODO */
    difference()
    {
      cylinder(d=160, h=5, center=true);
      cylinder(d=80, h=6, center=true);
    }
  }
}

BrakeDisc();
