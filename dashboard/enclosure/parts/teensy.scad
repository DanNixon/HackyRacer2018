pcb_dimensions = [61, 18, 1.6];

sd_card_dimensions = [16, 12, 2];
sd_card_overhang = 3;

module Teensy35()
{
  /* PCB */
  translate([0, -pcb_dimensions[1] / 2, 0])
  {
    color("darkgreen")
    {
      cube(pcb_dimensions);
    }
  }

  /* SD card */
  translate([-sd_card_overhang, -sd_card_dimensions[1] / 2, pcb_dimensions[2]])
  {
    color("silver")
    {
      cube(sd_card_dimensions);
    }
  }
}

module Teensy35SdCardCutout()
{
  size = [50, 20, 5];
  translate([-size[0] / 2, -size[1] / 2, 0])
  {
    cube(size);
  }
}

Teensy35();
