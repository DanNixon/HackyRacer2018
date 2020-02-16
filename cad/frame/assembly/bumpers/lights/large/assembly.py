import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import light, mount


def holes():
    return sp.rotate((0., 0., 180.))(
        sp.union()(
            light.holes(),
            spu.back((light.diameter / 2.) + 9.)(mount.holes()),
        )
    )


def assembly():
    return sp.rotate((0., 0., 180.))(
        sp.union()(
            sp.color("red")(spu.up(15.)(light.volume())),
            sp.color("green")(
                spu.back((light.diameter / 2.) + 9.)(mount.volume())
            ),
        )
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
