number_rows, number_columns = map(int, input().split())
matrix = []

for i in range(number_rows):
    matrix.append(list(map(int, input().split())))

for i in range(1, number_rows):
    for j in range(1, number_columns):
        matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]

for i in matrix:
    print(*i)
