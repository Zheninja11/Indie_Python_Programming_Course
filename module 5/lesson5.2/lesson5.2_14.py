n = int(input())
res = ''
for i in range(n):
    a = input().lower()
    if 'соль' in a:
        continue
    res += a
    res += ', '
print(res[:-2])
