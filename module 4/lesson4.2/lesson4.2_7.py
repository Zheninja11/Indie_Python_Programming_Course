number_1, number_2 = map(int, input().split())
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
list_3 = []
list_4 = list_1 + list_2
while list_4:
    list_3.append(list_4.pop(list_4.index(min(list_4))))
print(*list_3)
