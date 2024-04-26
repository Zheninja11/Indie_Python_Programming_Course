list_1 = list(map(int, input().split()))
min_number = min(list_1)
for i in range(len(list_1)):
    if min_number <= 0:
        list_1.remove(min(list_1))
        if not list_1:
            min_number = "Empty"
            break
        min_number = min(list_1)
    elif min_number > 0:
        break
print(min_number)
