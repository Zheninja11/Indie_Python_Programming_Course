n, m = map(int, input().split())

for j in range(n):
    print(' '.join([str(i + m * j) for i in range(m)][::pow(-1, j)]))