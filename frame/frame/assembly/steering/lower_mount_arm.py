import solid as sp
import solid.utils as spu

from frame.materials import flat_bar
from frame.primitives import drilled_hole
from frame.utils import entrypoint, place_at_centres, place_n_at_x_around

width = 50.
length = 75.
thickness = 8.

mounting_hole_diameter = 4.
mounting_hole_offset = 20.

tie_rod_hole_diameter = 5.
tie_rod_hole_centres = 35.
tie_rod_hole_offset = length - 6.


def place_mounting_holes(obj):
    return sp.rotate((0., 0., 60.))(
        place_n_at_x_around(3, mounting_hole_offset, obj)
    )


def volume():
    from . import lower_mount
    magic_1 = (lower_mount.face_diameter / 2.) - 5.

    bar = sp.translate((0., magic_1, thickness / 2.))(
        sp.rotate((90, 0, 0))(
            flat_bar.volume(length=length + magic_1, size=(width, thickness))
        )
    )

    mounting_holes = place_mounting_holes(
        drilled_hole.volume(mounting_hole_diameter)
    )

    tie_rod_holes = spu.back(tie_rod_hole_offset)(
        place_at_centres(
            (tie_rod_hole_centres, 0.),
            drilled_hole.volume(tie_rod_hole_diameter)
        )
    )

    return bar - mounting_holes - tie_rod_holes


if __name__ == '__main__':
    entrypoint.main(volume())
