def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

number_of_numbers = int(input())
numbers_list = [(int(input())) for number in range(number_of_numbers)]

gcd_list_of_numbers = dict()

for number_left in range(len(numbers_list)):
    for number_right in range(len(numbers_list) - 1, - 1, - 1):
        if number_left != number_right:
            gcd_list_of_numbers[f'{numbers_list[number_left]} % {numbers_list[number_right]}'] = gcd(numbers_list[number_left], numbers_list[number_right])

print(min(gcd_list_of_numbers.values(), key=lambda x: x))
