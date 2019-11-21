import solid as sp

from frame.utils import bom, place_n_at_x_around


def projection():
    outer = sp.circle(d=140)
    inner = sp.circle(d=38)
    mounting_holes = place_n_at_x_around(6, 24, sp.circle(d=6))
    return outer - inner - mounting_holes


@bom.part('Brake Disc')
def volume():
    return sp.linear_extrude(2)(projection())


if __name__ == '__main__':
    print(sp.scad_render(volume()))
