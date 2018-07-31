max_external_dimensions = [1500, 900, 1800];
original_kart_bounds = [1010, 590, 500];

color([0, 1, 0])
  cube(original_kart_bounds);

color([0, 1, 1, 0.5])
  cube(max_external_dimensions);
