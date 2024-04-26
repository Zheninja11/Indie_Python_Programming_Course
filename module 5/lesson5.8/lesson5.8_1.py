number_rows_and_columns = int(input())
matrix = []
numbers_side_diagonal = []

for i in range(number_rows_and_columns):
    matrix.append(list(map(int, input().split())))

for i in range(number_rows_and_columns):
    numbers_side_diagonal.append(matrix[i][number_rows_and_columns - 1 - i])

max_number_side_diagonal = max(numbers_side_diagonal)

print(max_number_side_diagonal)
