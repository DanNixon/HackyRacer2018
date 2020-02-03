import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import fan, shroud


def assembly():
    return sp.union()(
        sp.color('red')(shroud.volume()),
        sp.color('green')(
            sp.rotate((90, 0, 0))(spu.forward(fan.size[1] / 2.)(fan.volume()))),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
