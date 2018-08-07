use <RacerSprocket.scad>

RacerSprocket(
  chain_type = 1,
  teeth = 6,
  sprocket_round_dim = 25.5,
  key_screw_diameter = 3.9,
  key_screw_offset = 25,
  bore_diameter = 9.1,
  shaft_height = 30,
  shaft_height_outer = 10,
  shaft_diameter_inner = 9,
  shaft_diameter_outer = 25
);

cylinder(h=5, d=10);
