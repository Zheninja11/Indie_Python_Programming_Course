number_rows_and_columns = int(input())
list_set = []

for i in range(number_rows_and_columns):
    list_set.append(list(map(int, input().split())))

condition_symmetry = True

for i in range(number_rows_and_columns):
    for j in range(number_rows_and_columns):
        if list_set[i][j] != list_set[j][i]:
            condition_symmetry = False
            break

if condition_symmetry == True:
    print("Yes")
else:
    print("No")
