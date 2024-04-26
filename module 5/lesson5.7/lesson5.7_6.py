number_rows_and_columns = list(map(int,input().split()))
list_set = []

for i in range(number_rows_and_columns[0]):
    list_set.append(list(map(int,input().split())))

for i in range(number_rows_and_columns[0]):
    for j in range(number_rows_and_columns[1]):
        print(list_set[~i][j], end=' ')
    print()
