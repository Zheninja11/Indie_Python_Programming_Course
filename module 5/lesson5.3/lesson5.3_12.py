number_1 = input()
chet_s = 0
nechet_s = 0
for i in range(len(number_1)):
    if i % 2 == 0:
        chet_s += int(number_1[i])
    else:
        nechet_s += int(number_1[i])
if (chet_s - nechet_s) % 11 == 0:
    print("YES")
else:
    print("NO")
