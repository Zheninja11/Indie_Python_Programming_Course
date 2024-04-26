numbers = [int(number) for number in input().split()]
dict_set = {}


for i in range(len(numbers) - 2, - 1, - 1):
    if not dict_set:
        dict_set = {numbers[- 2]: numbers[- 1]}
    else:
        dict_set = {numbers[i]: dict_set}

print(dict_set)
