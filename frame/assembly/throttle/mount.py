import solid as sp

from frame.utils import entrypoint

from .dimensions import lever_thickness, mount_thickness, layer_spacing, pot_mount_diameter, mount_screw_diameter


def volume():
    mount_length = 20.
    mount_width = 15.

    magic_1 = 10.
    magic_2 = 30.

    return sp.difference()(
        sp.translate([0, 0, (lever_thickness / 2) - 0.1])(
            sp.rotate((0, 180, 0))(
                sp.linear_extrude(
                    mount_thickness + lever_thickness + layer_spacing
                )(
                    sp.difference()(
                        sp.hull()(
                            sp.circle(d=mount_width),
                            sp.translate((0, -(mount_length - 1)))(
                                sp.square((mount_width, 1), center=True)
                            )
                        ),
                        sp.circle(d=pot_mount_diameter, segments=32),
                    )
                )
            )
        ),

        sp.translate((0, 0, (lever_thickness - magic_1) / 2))(
            sp.cube((mount_width + 1, magic_2, magic_1), center=True),
            sp.rotate([90, 0, 0])(
                sp.cylinder(h=50, d=mount_screw_diameter, segments=16)
            )
        )
    )



if __name__ == '__main__':
    entrypoint.main(volume())
