def flatten_dict(a: dict, key: str = '') -> dict:
    c = {}
    for k, v in a.items():
        if type(v) == int:
            c.update({(key+'_'+k)[1:]: v})
        else:
            c.update(flatten_dict(v, key=key+'_'+k))
    return c
