letters = input()
numbers = [int(number) for number in letters if number.isdigit()]
dict_count_numbers = {}

for number in numbers:
    if number not in dict_count_numbers:
        dict_count_numbers[number] = 1
    else:
        dict_count_numbers[number] += 1

set_count_numbers = set()

for number in dict_count_numbers:
    if dict_count_numbers[number] > 1:
        set_count_numbers.add(number)

print(*set_count_numbers if set_count_numbers else ['NO'])
