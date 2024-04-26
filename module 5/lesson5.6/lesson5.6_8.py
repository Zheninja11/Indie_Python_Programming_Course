number_quantity = int(input())
list_set = list(map(int, input().split()))
length_list = len(list_set)

for i in range(1, length_list):
    for j in range(i, 0, -1):
        if list_set[j] < list_set[j - 1]:
            list_set[j - 1], list_set[j] = list_set[j], list_set[j - 1]
        else:
            break
print(*list_set)
