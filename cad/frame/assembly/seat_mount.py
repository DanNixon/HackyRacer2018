import solid as sp
import solid.utils as spu

from frame.utils import split_centers, place_at_centres
from frame.primitives.drilled_hole import volume as drilled_hole
from frame.materials import box_section, plate
from frame.utils import entrypoint

from .dimensions import outer

seat_depth = 300.
mount_bar_centres = 230.


def assembly():
    x_bars = sp.rotate([0, 90, 0])(
        [
            spu.back(d)(
                box_section.volume(
                    length=outer * 2. + box_section.default_size[0],
                    center=True
                )
            ) for d in split_centers(seat_depth)
        ]
    )

    y_bars = sp.rotate([90, 0, 0])(
        [
            spu.left(d)(
                box_section.volume(
                    length=seat_depth - box_section.default_size[0],
                    center=True
                )
            ) for d in [-outer, outer]
        ]
    )

    _mount_bar_centres = (mount_bar_centres - box_section.default_size[0]) / 2.
    mount_bars = spu.up(box_section.default_size[0])(
        sp.rotate([90, 0, 0])(
            [
                spu.left(d)(
                    box_section.volume(
                        length=seat_depth + box_section.default_size[0],
                        center=True
                    )
                ) for d in [-_mount_bar_centres, _mount_bar_centres]
            ]
        )
    )

    frame = sp.union()(
        sp.color('red')(x_bars),
        sp.color('green')(y_bars),
        sp.color('blue')(mount_bars),
    )

    return frame


if __name__ == '__main__':
    entrypoint.main(assembly())
