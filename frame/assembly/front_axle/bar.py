import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import inner
from frame.materials import box_section
from frame.utils import entrypoint, place_at_centres

from .stub_axle import camber

bar_length = (2. * inner) + box_section.default_size[0]

mount_overhang = 50.
mount_overlap = 50.
mount_length = 10.

magic_1 = mount_overlap + mount_length

# Note
# Mount bar is actuall one solid bar.
# It is constructed by:
# - Cut at an angle to the bottom bar removing a `camber` degree wdge
# - Bend so that wdge is closed and welded in position
# mount_bar_total_length = bar_length + (2. * magic_1)

d = box_section.default_size[0]


def mount():

    padding_bars = sp.color('green')(
        sp.translate((0, 0, -d))(
            sp.rotate((0, 90, 0))(
                box_section.volume(length=mount_overlap, center=False)
            )
        )
    )

    yoke_bars = sp.color('blue')(
        [
            sp.translate((-mount_overhang, 0, z))(
                sp.rotate((0, 90, 0))(
                    box_section.volume(
                        length=mount_overhang + mount_overlap, center=False
                    )
                )
            ) for z in [d, -d * 2.]
        ]
    )

    mount_bar = sp.color('cyan')(
        sp.rotate((0, 90, 0))(box_section.volume(length=magic_1, center=False))
    )

    return spu.left(bar_length / 2.)(
        sp.rotate((0, camber, 0))(
            sp.translate((-magic_1, 0, 0.5 * d))(
                sp.union()(
                    padding_bars,
                    yoke_bars,
                    mount_bar,
                )
            )
        )
    )


def assembly():
    main_bar = sp.rotate((0, 90, 0))(
        box_section.volume(length=bar_length, center=True)
    )

    return sp.union()(
        sp.color('red')(main_bar),
        spu.down(0.5 * d)(
            mount(),
            sp.rotate((0, 0, 180))(mount()),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
