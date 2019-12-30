import solid as sp

from frame.utils import entrypoint

from .common import outer_projection, place_mounting_holes
from .dimensions import size, box_depth

wall_thickness = 3.
mount_support_radius = 5.


def inner_projection():
    return sp.square([d - (2. * wall_thickness)
                      for d in size], center=True) - place_mounting_holes(
                          sp.circle(r=mount_support_radius, segments=16)
                      )


def projection():
    return outer_projection() - inner_projection()


def volume():
    return sp.linear_extrude(box_depth)(projection())


if __name__ == '__main__':
    entrypoint.main(volume())
