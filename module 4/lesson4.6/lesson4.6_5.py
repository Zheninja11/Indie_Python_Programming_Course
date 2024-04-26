a = int(input())
b = int(input())
a1 = a - 1
while a1 < b:
    a1 += 1
    if a1 % 2 == 0 or a1 % 3 == 0 and a1 != 777:
        continue
    elif a1 == 777:
        break
    print(a1)
