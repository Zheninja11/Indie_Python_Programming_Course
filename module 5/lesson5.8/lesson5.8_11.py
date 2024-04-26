n = int(input())
a = []
for i in range(n):
    a.append([0] * n)
count = 1
a[n // 2][n // 2] = n * n

for i in range(n // 2):
    for j in range(i, n - i):
        a[i][j] = count
        count += 1
    for j in range(i + 1, n - i):
        a[j][n-1-i] = count
        count += 1
    for j in range(n-2-i,-1+ i,-1):
        a[n-1-i][j] = count
        count += 1
    for j in range(n-2-i,i,-1):
        a[j][i] = count
        count += 1

for i in a:
    print(*i)
