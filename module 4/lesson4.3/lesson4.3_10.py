a = int(input())
s = 0
while a > 0:
    last = a % 10
    if last == 7:
        s += 1
    a = a // 10
print(s)
