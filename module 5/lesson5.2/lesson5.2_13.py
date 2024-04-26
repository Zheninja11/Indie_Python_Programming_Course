n = int(input())
for i in range(n):
    text = input().lower()
    s = text.find('рок') + 1
    if s > 0:
        print(i + 1, s)
