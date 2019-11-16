import solid as sp

from frame.utils import place_n_at_x_around

# XX tooth
outer_diameter = 140

# 74 tooth
# outer_diameter = 190;


def projection():
    outer = sp.circle(d=outer_diameter)
    inner = sp.circle(d=26)
    mounting_holes = place_n_at_x_around(3, 20, sp.circle(d=6))
    return outer - inner - mounting_holes


def drive_sprocket():
    return sp.linear_extrude(3)(projection())


if __name__ == '__main__':
    print(sp.scad_render(drive_sprocket()))
