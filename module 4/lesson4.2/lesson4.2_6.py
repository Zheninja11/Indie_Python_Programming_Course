n = int(input())
level = 0
cub_level = 0
s = 0
while s < n:
    level += 1
    cub_level += level
    s += cub_level
if s == n:
    print(level)
else:
    print(level - 1)
