s = input().lower()
t = input().lower()
s1 = s[::-1]
if t == s1:
    print('YES')
else:
    print('NO')
