from functools import wraps

def memoize(func):
    empty_dictionary = {}

    @wraps(func)
    def inner(*args, **kwargs):
        if args in empty_dictionary:
            return empty_dictionary[args]
        else:
            empty_dictionary[args] = func(*args)
            return empty_dictionary[args]
    
    return inner
