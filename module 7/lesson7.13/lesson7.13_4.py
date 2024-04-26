def create_accumulator(num: int = 0):
    sum_numbers = num

    def inner_func(number):
        nonlocal sum_numbers
        sum_numbers += number
        return sum_numbers
    
    return inner_func
