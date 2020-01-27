import solid as sp

from frame.utils import entrypoint, bom

from . import stub_axle, wheel

# TODO: measure what is actually needed here
length = 85.


def projection():
    return sp.circle(d=wheel.shaft_bore) - sp.circle(d=stub_axle.axle_diameter)


@bom.part('Front Wheel Bushing')
def volume():
    return sp.linear_extrude(length)(projection())


if __name__ == '__main__':
    entrypoint.main(volume())
