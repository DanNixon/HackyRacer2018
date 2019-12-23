import solid as sp
import solid.utils as spu

from frame.utils import entrypoint, place_at_centres

from . import bumper
from .dimensions import light_centres, light_y_offset
from .. import lights


def assembly():
    rear_lights = spu.forward(light_y_offset)(
        [
            place_at_centres([x, 0], lights.small.volume())
            for x in light_centres
        ]
    )

    return sp.union()(
        sp.color('red')(bumper.volume()),
        spu.up(bumper.thickness)(sp.color('green')(rear_lights), ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
