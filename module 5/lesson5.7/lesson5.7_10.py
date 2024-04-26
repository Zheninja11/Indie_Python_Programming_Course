number_athletes_and_throws = list(map(int, input().split()))
list_set = []
list_row_sum = []
number_row = 0

for i in range(number_athletes_and_throws[0]):
    list_set.append(list(map(int, input().split())))

for i in range(number_athletes_and_throws[0]):
    sum_row_loop = 0
    for j in range(number_athletes_and_throws[1]):
        sum_row_loop += list_set[i][j]
    list_row_sum.append(sum_row_loop)

print(max(list_row_sum))
print(list_row_sum.index(max(list_row_sum)))
