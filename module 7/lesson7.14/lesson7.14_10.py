def double_it(func):

    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    
    return inner
