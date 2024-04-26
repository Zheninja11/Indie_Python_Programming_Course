number_athletes_and_throws = list(map(int, input().split()))
list_set = []

for i in range(number_athletes_and_throws[0]):
    list_set.append(list(map(int, input().split())))

max_value = 0
counter = 0

for i in range(number_athletes_and_throws[0]):
    if max(list_set[i]) > max_value:
        max_value = max(list_set[i])

for i in range(number_athletes_and_throws[0]):
    is_best = False
    for j in range(number_athletes_and_throws[1]):
        if is_best == True:
            continue
        if list_set[i][j] == max_value:
            is_best = True
            counter += 1
print(counter)
