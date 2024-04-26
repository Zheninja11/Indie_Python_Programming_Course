def count_strings(*args):

    counter = 0

    for i in args:
        if isinstance(i, str):
            counter += 1

    return counter
