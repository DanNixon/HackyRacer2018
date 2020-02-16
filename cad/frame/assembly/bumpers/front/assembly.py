import solid as sp
import solid.utils as spu

from frame.utils import entrypoint, place_at_centres

from .dimensions import small_light_centres, small_light_y_offset, large_light_centres, large_light_y_offset
from . import bumper
from .. import lights


def assembly():
    small_lights = spu.forward(small_light_y_offset)(
        place_at_centres([small_light_centres, 0], lights.small.volume())
    )

    large_lights = spu.forward(large_light_y_offset)(
        place_at_centres([large_light_centres, 0], lights.large.assembly())
    )

    return sp.union()(
        sp.color('red')(bumper.volume()),
        spu.up(bumper.thickness)(
            sp.color('green')(small_lights),
            sp.color('blue')(large_lights),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
