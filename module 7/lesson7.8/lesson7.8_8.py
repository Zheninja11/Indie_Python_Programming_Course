def double_fact(number: int):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return number * double_fact(number - 2)
