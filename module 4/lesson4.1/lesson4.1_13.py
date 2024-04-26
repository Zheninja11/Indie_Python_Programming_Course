a, b = map(int, input().split())
day = 0
while a > 0:
    a -= 1
    day += 1
    if day % b == 0:
        a += 1
print(day)
