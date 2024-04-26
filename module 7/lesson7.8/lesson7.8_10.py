def tribonacci(number: int):
    if number == 0:
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return tribonacci(number - 1) + tribonacci(number - 2) + tribonacci(number - 3)
