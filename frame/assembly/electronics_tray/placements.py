import solid as sp


def arduino():
    return sp.translate((0, -30))


def bec_module():
    return sp.translate((0, 30))


def can_bus_board():
    return sp.translate((80, 30))


def lighting_control_board():
    return sp.translate((80, -30))


def relay_board():
    return sp.translate((0, 0))


def vesc():
    return sp.translate((-80, 0))
