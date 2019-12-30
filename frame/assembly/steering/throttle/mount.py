import solid as sp
import solid.utils as spu

from frame.assembly.steering.wheel import hand_grip_diameter
from frame.utils import entrypoint

from .dimensions import pot_offset

ring_length = 18.
ring_outer_diameter = 30.

split_ring_space = 3.
split_ring_screw_hole_diameter = 4.

pot_mount_diameter = 7.5
pot_mount_thickness = 5.

split_ring_additional_padding = 2.

magic_2 = (ring_outer_diameter / 2.)
magic_1 = magic_2 + split_ring_additional_padding


def volume():
    outer = sp.rotate((90, 0, 0))(
        sp.cylinder(
            d=ring_outer_diameter, h=ring_length, center=True, segments=32
        )
    ),

    inner = sp.rotate((90, 0, 0))(
        sp.cylinder(d=hand_grip_diameter, h=100., center=True, segments=32)
    )

    split_ring_padding = spu.down(magic_1 / 2.)(
        sp.cube((ring_outer_diameter, ring_length, magic_1), center=True)
    )

    split_ring_cutout = spu.down(
        magic_1 / 2.
    )(sp.cube((split_ring_space, ring_length + 2., magic_1 + 1.), center=True))

    split_ring_screw_hole = spu.down(magic_2 - 2.)(
        spu.rotate((0, 90, 0))(
            sp.cylinder(
                d=split_ring_screw_hole_diameter,
                h=ring_outer_diameter + 1.,
                center=True,
                segments=32
            )
        )
    )

    magic_4 = ring_length + split_ring_additional_padding
    pot_mount = spu.right(magic_2 - (pot_mount_thickness / 2.))(
        sp.hull()(
            sp.translate((0, 0, -magic_4 / 2.))
            (sp.cube((pot_mount_thickness, ring_length, magic_4), center=True)),
            sp.translate(pot_offset)
            (sp.cube((pot_mount_thickness, 15, 15), center=True)),
            sp.translate((0, 0, pot_offset[2]))
            (sp.cube((pot_mount_thickness, ring_length, 15), center=True)),
        ) - sp.translate(pot_offset)(
            sp.rotate((0, 90, 0))(
                sp.cylinder(
                    d=pot_mount_diameter,
                    h=pot_mount_thickness + 1.,
                    center=True,
                    segments=32
                )
            )
        )
    )

    return sp.union()(
        outer,
        split_ring_padding,
        pot_mount,
    ) - inner - split_ring_cutout - split_ring_screw_hole


if __name__ == '__main__':
    entrypoint.main(volume())
