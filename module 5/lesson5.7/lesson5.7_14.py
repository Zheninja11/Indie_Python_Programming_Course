matrix_size = 4
list_set = []

for i in range(matrix_size):
    list_set.append(list(input()))

result = "Yes"

for i in range(matrix_size - 1):
    for j in range(matrix_size - 1):
        if list_set[i][j] == list_set[i][j + 1] == list_set[i + 1][j] == list_set[i + 1][j + 1]:
            result = "No"

print(result)
