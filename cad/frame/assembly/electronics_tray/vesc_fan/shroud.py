import solid as sp
import solid.utils as spu

from frame.utils import entrypoint, place_at_centres

from . import fan

outer_wall_thickness = 6.
length = 120.

size = (
    fan.size[0] + (outer_wall_thickness * 2.),
    fan.size[1] + outer_wall_thickness
)


def mounting_holes(s):
    return spu.forward(length / 2.)(
        place_at_centres(
            (fan.size[0] + 6., length - 10.), sp.circle(d=3.1, segments=s)
        )
    )


def projection_outer():
    return spu.forward(outer_wall_thickness / 2.)(sp.square(size, center=True))


def projection_main():
    return projection_outer() - sp.square(fan.size, center=True)


def projection_fan():
    return projection_outer() - fan.main_vent() - fan.mounting_holes()


def volume():
    extrusion = sp.rotate((0, 0, 0))(
        sp.union()(
            spu.down(length)(sp.linear_extrude(length)(projection_main())),
            spu.down(10.)(sp.linear_extrude(10.)(projection_fan())),
        )
    )
    rotated_extrusion = sp.rotate((90, 0, 0))(
        spu.forward(fan.size[1] / 2.)(extrusion)
    )

    tray_mounting_holes = sp.linear_extrude(10.)(mounting_holes(6))

    def cable_cutout(position, diameter):
        return sp.translate(position)(
            sp.rotate((0, 90, 0))
            (sp.cylinder(d=diameter, h=outer_wall_thickness + 1., center=True))
        )

    cable_cutouts = sp.union()(
        cable_cutout((-33, 20, 15), 15.),
        cable_cutout((-33, 60, 10), 12.),
    )

    return rotated_extrusion - tray_mounting_holes - cable_cutouts


if __name__ == '__main__':
    entrypoint.main(volume())
