a = input().zfill(6)
d1 = int(a[0])
d2 = int(a[1])
d3 = int(a[2])
d4 = int(a[3])
d5 = int(a[4])
d6 = int(a[5])
if (d1 + d2 + d3) == (d4 + d5 + d6):
    print('YES')
else:
    print('NO')
