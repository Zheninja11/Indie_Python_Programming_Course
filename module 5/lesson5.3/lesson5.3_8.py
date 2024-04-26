list_1 = list(map(int, input().split()))
number_1 = int(input())
counter = 0
for i in range(len(list_1)):
    if list_1[i] == number_1:
        break
    counter += 1
if number_1 not in list_1:
    print("ErrorValue")
else:
    print(counter + 1)
