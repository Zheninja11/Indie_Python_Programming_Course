list_set = list(map(int, input().split()))
length_list = len(list_set)
result = True

for i in range(0, length_list - 1):
    if list_set[i] > list_set[i + 1]:
        result = False
    elif list_set[i] == list_set[i + 1]:
        continue
print(result)
