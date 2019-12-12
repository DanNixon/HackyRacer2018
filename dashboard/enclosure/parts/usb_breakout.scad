pcb_dimensions = [14, 12.5, 1.6];

usb_port_dimensions = [6, 8, 2];
usb_port_overhang = 1;

mounting_hole_diameter = 3.1;
mounting_hole_centres = 9;

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

    /* Mounting holes */
    for(y = [-mounting_hole_centres / 2, mounting_hole_centres / 2])
    {
      translate([pcb_dimensions[0] / 2, y, 0])
      {
        cylinder(d=mounting_hole_diameter, h=20, center=true, $fn=32);
      }
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

UsbBreakout();
