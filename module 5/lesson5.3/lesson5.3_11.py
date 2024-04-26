string_1 = input()
count_1 = 0
number_sum = 0
for i in range(len(string_1)):
    if string_1[i].isdigit():
        count_1 += 1
        number_sum += int(string_1[i])
print(count_1, number_sum)
