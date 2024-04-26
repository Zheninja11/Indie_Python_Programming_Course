string_1 = list(input().split())
string_2 = []
string_3 = []
for i in string_1:
    if i.lower() not in string_2:
        string_2.append(i.lower())
        string_3.append(i)
print(*string_3)
