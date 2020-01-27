import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import box, panel
from .dimensions import box_depth


def assembly():
    return sp.union()(
        sp.color('red')(box.volume()),
        sp.color('green')(spu.up(box_depth)(panel.volume())),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
