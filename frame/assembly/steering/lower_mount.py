import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import axle_diameter
from frame.primitives import drilled_hole
from frame.utils import entrypoint

face_width = 12
face_diameter = 50

clamp_width = 30
clamp_diameter = 32

length = face_width + clamp_width


def volume():
    face_plate = sp.cylinder(d=face_diameter, h=face_width)

    # Drill and tap holes for axle key screws as appropriate
    axle_clamp = sp.cylinder(d=clamp_diameter, h=length)

    axle = spu.down(1)(sp.cylinder(d=axle_diameter, h=length + 2))

    return sp.union()(face_plate, axle_clamp) - axle


if __name__ == '__main__':
    entrypoint.main(volume())
