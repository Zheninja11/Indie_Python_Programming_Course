a = int(input())
i = 0
while a != 1:
    if a % 2 == 0:
        a = a/2
    else:
        a = 3 * a + 1
    i += 1
print(i)
