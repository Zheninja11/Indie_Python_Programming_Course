number = int(input())
list_set = []
main_diagonal_sum = 0

for i in range(number):
    list_set.append(list(map(int,input().split())))
    for j in range(number):
        if i == j:
            main_diagonal_sum += list_set[i][j]
print(main_diagonal_sum)
