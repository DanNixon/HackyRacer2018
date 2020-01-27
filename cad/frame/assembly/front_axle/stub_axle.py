import solid as sp
import solid.utils as spu

# TODO: measure this
camber = 10.

axle_diameter = 17.
tie_rod_hole_diameter = 8.


def tie_rod_plate():
    def pt(x, y, r=1.):
        return sp.translate((x, y))(sp.circle(r=r, segments=16))

    magic_1 = (40., 72.)
    magic_2 = (5., 60.)

    tie_rod_hole_1 = (-5., 102.)
    tie_rod_hole_2 = (-20., 102.)

    return sp.linear_extrude(6.)(
        sp.difference()(
            sp.union()(
                sp.hull()(
                    pt(5., 0.),
                    pt(45., 0.),
                    pt(*magic_1),
                    pt(*magic_2),
                ),
                sp.hull()(
                    pt(*magic_1),
                    pt(*magic_2),
                    pt(*tie_rod_hole_1, r=7.),
                    pt(*tie_rod_hole_2, r=7.),
                    pt(-5., 85.),
                ),
            ),
            pt(*tie_rod_hole_1, r=tie_rod_hole_diameter / 2.),
            pt(*tie_rod_hole_2, r=tie_rod_hole_diameter / 2.),
        )
    )


def axle():
    return sp.union()(
        sp.cylinder(h=165., d=12.),
        sp.cylinder(h=145., d=axle_diameter),
        sp.cylinder(h=55., d=22.),
        sp.rotate((0., -90., 0.))(tie_rod_plate()),
    )


def kingpin_hole():
    return sp.cylinder(h=100., d=8., center=True)


def bearing_housing():
    return sp.cylinder(h=40., d=34., center=True)


def volume(angle_multiplier):
    return sp.difference()(
        sp.union()(
            sp.rotate((0., angle_multiplier * 90., 180.))(axle()),
            sp.rotate((0., angle_multiplier * camber, 0.))(bearing_housing()),
        ),
        sp.rotate((0., angle_multiplier * camber, 0.))(kingpin_hole()),
    )
