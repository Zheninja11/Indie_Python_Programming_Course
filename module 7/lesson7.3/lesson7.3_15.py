def factorial(number):
    fact = 1
    for num in range(2, number + 1):
        fact *= num
    return list(str(fact))


def trailing_zeros(num):
    fact_list = factorial(num)
    zeros_counter = 0

    for i in range(len(fact_list) - 1, - 1, - 1):
        if fact_list[i] == '0':
            zeros_counter += 1
        else:
            break
    
    return zeros_counter
