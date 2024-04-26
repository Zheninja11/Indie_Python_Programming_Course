n, m = map(int, input().split())

is_color = False

for i in range(n):
    row = input().split()
    for color in row:
        if color in ['C', 'M', 'Y']:
            is_color = True
            break
    if is_color:
        break

if is_color:
    print("#Color")
else:
    print("#Black&White")
