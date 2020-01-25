import solid as sp


def bec_module(obj):
    return sp.translate((0., 40.))(sp.rotate((0., 0., 90.))(obj))


def lighting_control_board(obj):
    return sp.translate((-80., -30.))(obj)


def logic_board(obj):
    return sp.translate((-80., 30.))(obj)


def relay_board(obj):
    return sp.translate((0., -20.))(obj)


def vesc(obj):
    return sp.translate((80., 0.))(obj)
