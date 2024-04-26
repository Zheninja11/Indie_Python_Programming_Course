def find_keys(**kwargs):

    sp = []

    for i in kwargs:
        if isinstance(kwargs[i], list) or isinstance(kwargs[i], tuple):
            sp.append(str(i))

    return sorted(sp, key=str.lower)
