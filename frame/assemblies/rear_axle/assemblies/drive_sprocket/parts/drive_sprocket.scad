module DriveSprocket()
{
  $fn = 64;

  color("cyan")
  {
    /* TODO */
    difference()
    {
      cylinder(d=180, h=5, center=true);
      cylinder(d=50, h=6, center=true);
    }
  }
}

DriveSprocket();
