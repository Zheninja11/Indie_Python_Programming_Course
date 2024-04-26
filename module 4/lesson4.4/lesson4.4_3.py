number = int(input())
i = 1
list_1 = []
while i ** 2 <= number:
    if number % i == 0:
        if i == number // i:
            list_1.append(i)
        else:
            list_1.append(i)
            list_1.append(number // i)
    i += 1
if len(list_1) == 2:
    print("Yes")
else:
    print("No")
