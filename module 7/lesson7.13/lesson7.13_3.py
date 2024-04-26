def create_accumulator():
    sum_numbers = 0

    def inner_func(number):
        nonlocal sum_numbers
        sum_numbers += number
        return sum_numbers
    
    return inner_func
