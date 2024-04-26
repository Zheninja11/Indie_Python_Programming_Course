def factorial(number_positive : int):
    result = 1
    for number in range(1, number_positive + 1):
        result *= number
    return result
