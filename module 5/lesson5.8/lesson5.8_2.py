number_rows_and_columns = int(input())
matrix = []
numbers_above_main_diagonal, numbers_below_main_diagonal, numbers_main_diagonal = map(int, input().split())

matrix = [[0]*number_rows_and_columns for i in range(number_rows_and_columns)]

for i in range(number_rows_and_columns):
    for j in range(number_rows_and_columns):
        if i == j:
            matrix[i][j] = numbers_main_diagonal
        elif i > j:
            matrix[i][j] = numbers_below_main_diagonal
        elif i < j:
            matrix[i][j] = numbers_above_main_diagonal

for row in matrix:
    print(*row)
