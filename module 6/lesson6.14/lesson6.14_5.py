number_card = list(map(int, input()))

for index, value in enumerate(number_card):
    if index % 2 == 0:
        if value * 2 > 9:
            number_card[index] = number_card[index] * 2 - 9
        else:
            number_card[index] = number_card[index] * 2

print('True') if sum(number_card) % 10 == 0 else print('False')
