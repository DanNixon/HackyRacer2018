import solid as sp
import solid.utils as spu

from frame.assembly import axle_diameter
from frame.utils import entrypoint
import frame.parts.drive_sprocket as drive_sprocket
import frame.parts.drive_sprocket_mount as drive_sprocket_mount


def assembly():
    return sp.union()(
        sp.color('red')(drive_sprocket_mount.volume()),
        sp.color('green')(
            spu.down(drive_sprocket.thickness)(drive_sprocket.volume())
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
