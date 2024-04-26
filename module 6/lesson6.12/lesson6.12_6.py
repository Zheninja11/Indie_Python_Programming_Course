numbers_list = int(input())
lists = [list(map(int, input().split())) for _ in range(numbers_list)]
set_numbers = []

for numbers in lists:
    for number in numbers:
        set_numbers.append(number)

print(len(set(set_numbers)))
