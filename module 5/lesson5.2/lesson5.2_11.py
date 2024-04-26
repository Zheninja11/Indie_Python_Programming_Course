n = int(input())
pr = 1
for i in range(1, n + 1):
    if n >= 2:
        pr = pr * i
    elif n == 0 or n == 1:
        pr = 1
print(pr)
