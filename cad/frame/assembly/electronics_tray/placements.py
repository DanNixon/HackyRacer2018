import solid as sp


def bec_module(obj):
    return sp.translate((-10., 40.))(sp.rotate((0., 0., 90.))(obj))


def lighting_control_board(obj):
    return sp.translate((-90., -30.))(obj)


def logic_board(obj):
    return sp.translate((-90., 30.))(obj)


def relay_board(obj):
    return sp.translate((-10., -20.))(obj)


def vesc(obj):
    return sp.translate((70., 0.))(obj)


def vesc_fan(obj):
    return sp.translate((70., -70.))(obj)
