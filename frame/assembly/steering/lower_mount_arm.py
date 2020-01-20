import solid as sp
import solid.utils as spu

from frame.materials import flat_bar
from frame.primitives import drilled_hole
from frame.utils import entrypoint, place_at_centres

from . import lower_mount

width = 50.
length = 75.
thickness = 8.

magic_1 = (lower_mount.face_diameter / 2.) - 5.

mounting_hole_diameter = 4.
mounting_hole_centres = 2. * (magic_1 - 8.)

tie_rod_hole_diameter = 4.
tie_rod_hole_offset = length - 6.


def place_mounting_holes(obj):
    return place_at_centres((0., mounting_hole_centres), obj)


def volume():
    bar = sp.translate((0., magic_1, 4.))(
        sp.rotate((90, 0, 0))(
            flat_bar.volume(length=length + magic_1, size=(width, thickness))
        )
    )

    return bar - place_mounting_holes(
        drilled_hole.volume(mounting_hole_diameter)
    ) - spu.back(tie_rod_hole_offset)(
        drilled_hole.volume(tie_rod_hole_diameter)
    )


if __name__ == '__main__':
    entrypoint.main(volume())
