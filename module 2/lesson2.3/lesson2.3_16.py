s = input().lower().replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '').replace('', '.')
s1 = len(s) - 1
print(s[:s1])
