class hashabledict(dict):
    def __key(self):
        return tuple((k, self[k]) for k in sorted(self))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()


g_parts_dict = {}


def part():
    def wrap(f):
        def wrapped_f(*wargs, **wkwargs):
            key = hashabledict(
                {
                    'name': '{}.{}'.format(f.__module__, f.__name__),
                }
            )
            key.update(**wkwargs)

            if key not in g_parts_dict:
                g_parts_dict[key] = 0
            g_parts_dict[key] += 1

            return f(*wargs, **wkwargs)

        return wrapped_f

    return wrap


def bill_of_materials():
    return g_parts_dict
