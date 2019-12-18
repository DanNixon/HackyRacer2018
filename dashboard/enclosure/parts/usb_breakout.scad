pcb_dimensions = [14, 12.5, 1.6];

usb_port_dimensions = [6, 8, 2];
usb_port_overhang = 1;

mounting_hole_diameter = 3.1;
mounting_hole_centres = 9;

module UsbBreakoutHoles()
{
  for(y = [-mounting_hole_centres / 2, mounting_hole_centres / 2])
  {
    translate([pcb_dimensions[0] / 2, y, 0])
    {
      circle(d=mounting_hole_diameter, $fn=32);
    }
  }
}

module UsbBreakout()
{
  difference()
  {
    /* PCB */
    translate([0, -pcb_dimensions[1] / 2, 0])
    {
      color("green")
      {
        cube(pcb_dimensions);
      }
    }

    linear_extrude(20, center=true)
    {
      UsbBreakoutHoles();
    }
  }

  /* USB port */
  translate([-usb_port_overhang, -usb_port_dimensions[1] / 2, pcb_dimensions[2]])
  {
    color("silver")
    {
      cube(usb_port_dimensions);
    }
  }
}

module UsbBreakoutCutout()
{
  size = [50, pcb_dimensions[1] + 1, 6];
  translate([-size[0] / 2, -size[1] / 2, -1])
  {
    cube(size);
  }
}

UsbBreakout();
