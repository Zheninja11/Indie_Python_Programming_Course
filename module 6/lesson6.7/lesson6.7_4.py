row = input().lower()
numbers_letter = {}
eng_dict = "abcdefghijklmnopqrstuvwxyz"

for i in row:
    if i in eng_dict:
        if i in numbers_letter:
            numbers_letter[i] += 1
        else:
            numbers_letter[i] = 1
    else:
        continue

print(numbers_letter)
