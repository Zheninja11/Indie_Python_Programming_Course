number_athletes_and_throws = list(map(int, input().split()))
list_set = []

for i in range(number_athletes_and_throws[0]):
    list_set.append(list(map(int, input().split())))

max_value_in_cycle = 0
row_max_value = 0
column_max_value = 0

for i in range(number_athletes_and_throws[0]):
    for j in range(number_athletes_and_throws[1]):
        if list_set[i][j] > max_value_in_cycle:
            max_value_in_cycle = list_set[i][j]
            row_max_value = i
            column_max_value = j

print(max_value_in_cycle)
print(row_max_value, column_max_value, end=' ')
