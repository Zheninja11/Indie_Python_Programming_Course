a = int(input())
s = 1
while a > 0:
    last = a % 10
    s = s * last
    a = a // 10
print(s)
