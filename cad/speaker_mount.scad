$fn = 32;

module MountTriangle(base, length, angle)
{
  linear_extrude(base, center=true)
  {
    hull()
    {
      circle(r=1);

      translate([base, 0, 0])
      {
        circle(r=1);
      }

      rotate([0, 0, -angle])
      {
        translate([0, length, 0])
        {
          circle(r=1);
        }
      }
    }
  }
}

module AngledMount(base, length, angle)
{
  difference()
  {
    MountTriangle(base, length, angle);

    translate([5, 4, 0])
    {
      MountTriangle(base - 5, length, angle);
    }

    rotate([0,0,  -90-angle])
    {
      for(x=[-20, 20])
      {
        translate([-length / 2, 0, x])
        {
          rotate([-90, 0, 0])
          {
            cylinder(h=10, d=4, center=true);
          }
        }
      }
    }
  }
}

module SpeakerCutout()
{
  circle(d=48);

  for(a=[45,135,225,315])
  {
    rotate([0, 0, a])
    {
      translate([30, 0])
      {
        circle(d=5);
      }
    }
  }
}

difference()
{
  rotate([0, -90, 0])
  {
    rotate([0, 0, -90])
    {
      AngledMount(65, 30, 15);
    }
  }

  translate([0, -35, -5])
  {
    linear_extrude(10)
    {
      SpeakerCutout();
    }
  }
}
