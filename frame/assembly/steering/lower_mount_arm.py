import solid as sp
import solid.utils as spu

from frame.materials import flat_bar
from frame.primitives import drilled_hole
from frame.utils import entrypoint, place_at_centres

from . import lower_mount

length = 75.
thickness = flat_bar.default_size[1]

magic_1 = (lower_mount.face_diameter / 2.) - 5.

mounting_hole_diameter = 4.
mounting_hole_centres = 2. * (magic_1 - 8.)

tie_rod_hole_diameter = 4.
tie_rod_hole_offset = length - 6.


def place_mounting_holes(obj):
    return place_at_centres((0., mounting_hole_centres), obj)


def volume():
    return sp.translate((0., magic_1, thickness / 2.))(
        sp.rotate((90, 0, 0))(flat_bar.volume(length=length + magic_1))
    ) - place_mounting_holes(drilled_hole.volume(mounting_hole_diameter)
                            ) - spu.back(tie_rod_hole_offset)(
                                drilled_hole.volume(tie_rod_hole_diameter)
                            )


if __name__ == '__main__':
    entrypoint.main(volume())
