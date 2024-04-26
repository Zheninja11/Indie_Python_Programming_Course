def multiply(num: int = 0):
    multi = num

    def inner_func(number):
        nonlocal multi
        return multi * number
    
    return inner_func
