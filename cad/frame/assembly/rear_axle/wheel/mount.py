import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import axle_diameter
from frame.utils import bom, entrypoint, place_n_at_x_around

from . import wheel

a_length = 15.

b_diameter = 84.
b_length = 20.

c_diameter = 55.
c_length = 30.


def volume():
    body = sp.union()(
        sp.rotate((0, 180, 0))(sp.cylinder(d=wheel.inner_hole_diameter, h=a_length)),
        sp.cylinder(d=b_diameter, h=b_length),
        sp.cylinder(d=c_diameter, h=b_length + c_length)
    )

    axle = sp.cylinder(d=axle_diameter, h=200., center=True)

    return sp.rotate((0, 90, 0))(body - axle - wheel.mounting_holes())


if __name__ == '__main__':
    entrypoint.main(volume())
