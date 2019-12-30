import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import axle_diameter, wheel_centre_distance
from frame.assembly import wheel
from frame.materials import round_bar
from frame.utils import entrypoint, place_at_centres

from . import brake_disc, drive_sprocket

sprocket_pos = 147.
brake_disc_pos = 160.

axle_length = wheel_centre_distance + 120.


def assembly():
    axle = sp.color('red')(
        round_bar.volume(
            diameter=axle_diameter, length=axle_length, center=True
        )
    )

    sprocket_assy = spu.down(sprocket_pos)(
        sp.color('green')(drive_sprocket.assembly())
    )

    brake_disc_assy = spu.up(brake_disc_pos)(
        sp.color('blue')(sp.rotate((180, 0, 0))(brake_disc.assembly()))
    )

    wheels = [
        sp.rotate([0, a,
                   0])(spu.right(wheel_centre_distance / 2.)(wheel.volume()))
        for a in [0, 180]
    ]

    return sp.union()(
        sp.rotate([0, 90,
                   0])(sp.union()(
                       axle,
                       sprocket_assy,
                       brake_disc_assy,
                   )),
        wheels,
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
