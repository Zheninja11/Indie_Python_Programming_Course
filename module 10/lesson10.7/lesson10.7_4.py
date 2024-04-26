text = input().lower().split()
flag = []

for i in text:
    if 'a' in i:
        flag.append(True)
    else:
        flag.append(False)

print(all(flag))
