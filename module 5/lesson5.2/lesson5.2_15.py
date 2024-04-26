n = int(input())
for i in range(1, n + 1):
    a = input()
    if len(a) < 10:
        print(a)
    elif len(a) > 10:
        a1 = str(len(a[1:-1]))
        print(a[0] + a1 + a[-1])
