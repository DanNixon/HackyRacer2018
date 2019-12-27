import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from .dimensions import pot_offset

ring_length = 18.
ring_outer_diameter = 30.
ring_inner_diameter = 20.

split_ring_space = 3.
split_ring_screw_hole_diameter = 4.

pot_mount_diameter = 7.5
pot_mount_thickness = 4.

split_ring_additional_padding = 2.

magic_2 = (ring_outer_diameter / 2.)
magic_1 = magic_2 + split_ring_additional_padding
magic_4 = 10.
magic_3 = pot_offset + magic_4
magic_5 = 4. - magic_2


def volume():
    outer = sp.rotate((90, 0, 0))(
        sp.cylinder(
            d=ring_outer_diameter, h=ring_length, center=True, segments=32
        )
    ),

    inner = sp.rotate((90, 0, 0))(
        sp.cylinder(
            d=ring_inner_diameter, h=ring_length + 1., center=True, segments=32
        )
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

    pot_mount = sp.difference()(
        sp.translate((magic_5, 0, -magic_2 - ((magic_3 - magic_2) / 2.)))(
            sp.cube(
                (pot_mount_thickness, ring_length + 10., magic_3 - magic_2),
                center=True
            )
        ),
        sp.translate((0, -2., -pot_offset))(
            spu.rotate((0, 90, 0))(
                sp.cylinder(
                    d=pot_mount_diameter,
                    h=ring_outer_diameter + 1.,
                    center=True,
                    segments=32
                )
            )
        ),
    )

    _blanking_offset = (ring_length / 2.) + 50.
    blanking = [
        sp.translate((0, y, 0))(sp.cube((100., 100., 100.), center=True))
        for y in (-_blanking_offset, _blanking_offset)
    ]

    return sp.union()(
        outer,
        split_ring_padding,
        sp.rotate((0, 0, -5))(pot_mount),
    ) - inner - split_ring_cutout - split_ring_screw_hole - blanking


if __name__ == '__main__':
    entrypoint.main(volume())
