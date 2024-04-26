string_1 = input()
counter = 0
for i in range(len(string_1)):
    if counter < 0:
        break
    elif string_1[i] == "(":
        counter += 1
    elif string_1[i] == ")":
        counter -= 1
if counter == 0:
    print("YES")
else:
    print("NO")
