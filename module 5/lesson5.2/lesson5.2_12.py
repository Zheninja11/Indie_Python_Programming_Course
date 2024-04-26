n = int(input())
m1 = 0
c1 = 0
for i in range(n):
    m2, c2 = map(int, input().split())
    if m2 > c2:
        m1 += 1
    elif m2 < c2:
        c1 += 1
    elif m2 == c2:
        m1 = m1
        c1 = c1
if m1 > c1:
    print('Mishka')
elif m1 < c1:
    print('Chris')
elif m1 == c1:
    print('Friendship is magic!^^')
