import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import axle_diameter
from frame.primitives import drilled_hole
from frame.utils import entrypoint

from . import wheel

face_width = 15
face_diameter = 60

clamp_width = 36
clamp_diameter = 32


def volume():
    face_plate = sp.cylinder(d=face_diameter, h=face_width)

    # Drill and tap holes for axle key screws as appropriate
    axle_clamp = sp.cylinder(d=clamp_diameter, h=face_width + clamp_width)

    axle = spu.down(1)(
        sp.cylinder(d=axle_diameter, h=face_width + clamp_width + 2)
    )

    # Drill and tap holes for brake disc mounting as appropriate
    mounting_holes = wheel.place_mounting_holes(drilled_hole.volume(5))

    return sp.union()(face_plate, axle_clamp) - axle - mounting_holes


if __name__ == '__main__':
    entrypoint.main(volume())
