import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from .common import outer_projection, place_mounting_holes
from .dimensions import size, corner_radius, box_depth

wall_thickness = 3.
mount_support_radius = 4.

magic_1 = (size[1] - 15.) / 2.


def inner_projection():
    return sp.square([d - (2. * wall_thickness)
                      for d in size], center=True) - place_mounting_holes(
                          sp.circle(r=mount_support_radius, segments=16)
                      )


def projection():
    return sp.union()(
        outer_projection(3., segments=5) - inner_projection(),
        spu.forward(magic_1)(sp.square((10., 15.), center=True)),
    )


def volume():
    width = 6.
    height = 6.

    cable_exit = sp.translate((0., magic_1, 0.))(
        sp.cube((width, 20., height * 2), center=True)
    )

    return sp.linear_extrude(box_depth)(projection()) - cable_exit


if __name__ == '__main__':
    entrypoint.main(volume())
