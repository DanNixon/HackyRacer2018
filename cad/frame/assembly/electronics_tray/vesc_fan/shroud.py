import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import fan

outer_wall_thickness = 5.
length = 100.

size = (
    fan.size[0] + (outer_wall_thickness * 2.),
    fan.size[1] + outer_wall_thickness
)
magic_1 = 2.
inner_size = (fan.size[0] - (magic_1 * 2.), fan.size[1] - magic_1)


def projection():
    # TODO
    return spu.forward(outer_wall_thickness / 2.)(
        sp.square(size, center=True)
    ) - spu.back(magic_1)(sp.square(inner_size, center=True))


def volume():
    extrusion = sp.rotate((0, 0, 0))(
        spu.down(length)(sp.linear_extrude(length)(projection()))
    )
    return extrusion


if __name__ == '__main__':
    entrypoint.main(volume())
