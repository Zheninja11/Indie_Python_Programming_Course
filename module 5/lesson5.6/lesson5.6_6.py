n = int(input())
list_set = list(map(int, input().split()))
count_list_set = 0

for i in range(n):
    for j in range(n - 1):
        if list_set[j] > list_set[j + 1]:
            count_list_set += 1
            list_set[j], list_set[j + 1] = list_set[j + 1], list_set[j]
print(*list_set)
print(count_list_set)
