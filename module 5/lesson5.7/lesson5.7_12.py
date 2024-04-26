number_athletes_and_throws = list(map(int, input().split()))
list_set = []

for i in range(number_athletes_and_throws[0]):
    list_set.append(list(map(int, input().split())))

max_value_in_cycle = 0
row_max_value = 0
max_value_sum_list = 0

for i in range(number_athletes_and_throws[0]):
    sum_of_elements = sum(list_set[i])
    for j in range(number_athletes_and_throws[1]):
        current_value = list_set[i][j]
        if current_value > max_value_in_cycle or (current_value == max_value_in_cycle and sum_of_elements > max_value_sum_list):
            max_value_in_cycle = list_set[i][j]
            row_max_value = i
            max_value_sum_list = sum_of_elements

print(row_max_value)
