from functools import wraps

def validate_args(func):

    @wraps(func)
    def inner(*args, **kwargs):
        if len(args) != 2:
            return 'Not enough arguments' if len(args) < 2 else 'Too many arguments'
        elif not all(isinstance(arg, int) for arg in args):
            return 'Wrong types'
        else:
            return func(*args, **kwargs)
        
    return inner
