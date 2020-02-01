import solid as sp
import solid.utils as spu

from frame.primitives import drilled_hole
from frame.utils import entrypoint

from .dimensions import column_diameter
from . import arm

face_width = 12.
face_diameter = 50.

clamp_width = 30.
clamp_diameter = 28.

length = face_width + clamp_width


def volume():
    face_plate = sp.cylinder(d=face_diameter, h=face_width)

    # Drill and tap holes for column key screws as appropriate
    column_clamp = sp.cylinder(d=clamp_diameter, h=length)

    column = spu.down(1)(sp.cylinder(d=column_diameter, h=length + 2))

    mounting_holes = arm.place_mounting_holes(
        drilled_hole.volume(arm.mounting_hole_diameter)
    )

    return sp.union()(face_plate, column_clamp) - column - mounting_holes


if __name__ == '__main__':
    entrypoint.main(volume())
