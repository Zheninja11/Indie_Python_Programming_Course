number_rows_and_columns = list(map(int,input().split()))
list_set = []
list_set_sum_rows = []
list_set_sum_columns = []

for i in range(number_rows_and_columns[0]):
    list_set.append(list(map(int, input().split())))

for i in range(number_rows_and_columns[0]):
    rows_sum = 0
    for j in range(number_rows_and_columns[1]):
        rows_sum += list_set[i][j]
    list_set_sum_rows.append(rows_sum)

for i in range(number_rows_and_columns[1]):
    columns_sum = 0
    for j in range(number_rows_and_columns[0]):
        columns_sum += list_set[j][i]
    list_set_sum_columns.append(columns_sum)

print(*list_set_sum_rows)
print(*list_set_sum_columns)
