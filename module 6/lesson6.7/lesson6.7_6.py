row_s1 = input()
row_s2 = input()
dict_row_s1 = {}
dict_row_s2 = {}

for i in row_s1:
    if i in dict_row_s1:
        dict_row_s1[i] += 1
    else:
        dict_row_s1[i] = 1

for i in row_s2:
    if i in dict_row_s2:
        dict_row_s2[i] += 1
    else:
        dict_row_s2[i] = 1

if dict_row_s1 == dict_row_s2:
    print('YES')
else:
    print('NO')
