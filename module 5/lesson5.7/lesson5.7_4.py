matrix_size = int(input())
list_set = []


for i in range(matrix_size):
    list_set.append(list(map(int,input().split())))

for i in range(matrix_size):
    for j in range(matrix_size):
        print(list_set[~j][~i], end=' ')
    print()
