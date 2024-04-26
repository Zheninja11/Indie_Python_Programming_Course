def get_combin(number_one: int, number_two: int) -> int:
    if number_two == 0:
        return 1
    elif number_two == number_one:
        return 1
    elif 0 < number_two < number_one:
        return get_combin(number_one - 1, number_two) + get_combin(number_one - 1, number_two - 1)
