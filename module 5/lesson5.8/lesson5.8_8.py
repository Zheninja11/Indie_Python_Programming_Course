number_rows, number_columns = map(int, input().split())
matrix = []

for i in range(number_rows):
    matrix.append(list(map(int, input().split())))

for i in range(number_rows - 1, -1, -1):
    for j in range(number_columns - 1, -1, -1):
        if matrix[i][j] == 0 and i < number_rows - 1 and j < number_columns - 1 and matrix[i + 1][j] != 0 and matrix[i][j + 1] != 0:
            matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]

for row in matrix:
    print(*row)
