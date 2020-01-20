import solid as sp
import solid.utils as spu

from frame.utils import bom


def projection(size, radius=3., center=True):
    return sp.minkowski()(
        sp.square([a - 2. * radius for a in size], center=center),
        sp.circle(r=radius),
    )


@bom.part('Plate')
def volume(size, thickness, radius=3., center=True):
    return sp.linear_extrude(thickness)(projection(size, radius, center))


if __name__ == '__main__':
    print(sp.scad_render(volume(size=(100, 50), thickness=3)))
