def fibonacci_number(number: int):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonacci_number(number - 1) + fibonacci_number(number - 2)

print(fibonacci_number(int(input())))
