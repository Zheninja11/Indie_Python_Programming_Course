def generate_fizz_buzz_list(number : int):
    result_list = []
    for num in range(1, number + 1):
        if num % 3 == 0 and num % 5 == 0:
            result_list.append('FizzBuzz')
        elif num % 3 == 0:
            result_list.append('Fizz')
        elif num % 5 == 0:
            result_list.append('Buzz')
        else:
            result_list.append(num)
    return result_list
