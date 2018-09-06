module PlaceUsbBoardHoles()
{
  dx = 8 / 2;

  for(x=[-dx, dx])
  {
    translate([x, 0])
    {
      children();
    }
  }
}

module UsbBoard()
{
  color("blue")
  {
    linear_extrude(3)
    {
      difference()
      {
        square([12.5, 14], center=true);

        PlaceCanTranscieverBoardHoles()
        {
          circle(d=3, $fn=16);
        }
      }
    }
  }
}

module PlaceCanTranscieverBoardHoles()
{
  dx = 8.5 / 2;

  for(x=[-dx, dx])
  {
    translate([x, -9.4])
    {
      children();
    }
  }
}

module CanTranscieverBoard()
{
  color("red")
  {
    linear_extrude(3)
    {
      difference()
      {
        square([11.5, 22.5], center=true);

        PlaceCanTranscieverBoardHoles()
        {
          circle(d=2, $fn=16);
        }
      }
    }
  }
}

module PlaceAmplifierBoardHoles()
{
  dx = 23 / 2;

  for(x=[-dx, dx])
  {
    translate([x, -9.6])
    {
      children();
    }
  }
}

module AmplifierBoard()
{
  color("blue")
  {
    linear_extrude(3)
    {
      difference()
      {
        square([28.3, 24.2], center=true);

        PlaceAmplifierBoardHoles()
        {
          circle(d=2.5, $fn=16);
        }
      }
    }
  }
}

module Teensy35Board()
{
  color("green")
  {
    linear_extrude(3)
    {
      square([17.8, 61], center=true);
    }
  }
}

module PlaceBecModuleHoles()
{
  dx = 28 / 2;
  dy = 25 / 2;

  for(x=[-dx, dx])
  {
    for(y=[-dy, dy])
    {
      translate([x, y])
      {
        children();
      }
    }
  }
}

module BecModule()
{
  color("lime")
  {
    linear_extrude(17)
    {
      square([26, 60], center=true);
    }
  }
}
