def flatten(sp: list) -> list:
    new = []
    for i in sp:
        if type(i) is int:
            new.append(i)
        else:
            new += flatten(i)
    return new
