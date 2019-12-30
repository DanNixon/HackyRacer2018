import solid as sp

from frame.utils import entrypoint

from .common import outer_projection, place_mounting_holes
from .dimensions import size, corner_radius, box_depth

wall_thickness = 2.
mount_support_radius = 4.


def inner_projection():
    return sp.square([d - (2. * wall_thickness)
                      for d in size], center=True) - place_mounting_holes(
                          sp.circle(r=mount_support_radius, segments=16)
                      )


def projection():
    return outer_projection() - inner_projection()


def volume():
    cable_exit = sp.translate((-size[0] / 2., (size[1] / 2.) - 12., 0))(
        sp.cube((10., 5., 5.), center=True)
    )

    return sp.linear_extrude(box_depth)(projection()) - cable_exit


if __name__ == '__main__':
    entrypoint.main(volume())
