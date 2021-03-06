import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from .. import bearing
from ..dimensions import thickness

from . import mount


def assembly():
    return sp.union()(
        sp.color("red")(mount.volume()),
        spu.down((thickness / 2.) + bearing.height)(
            sp.color("green")(bearing.volume())
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
