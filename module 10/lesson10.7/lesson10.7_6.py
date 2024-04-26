text = input().lower().split()
flag = []

for i in text:
    if i.endswith('ought'):
        flag.append(True)
    else:
        flag.append(False)

print(any(flag))
