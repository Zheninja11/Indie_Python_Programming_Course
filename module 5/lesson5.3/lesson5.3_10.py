test_string = input().lower()
variable = 0
variable_2 = 0
for i in range(len(test_string)):
    variable_2 = test_string.count(test_string[i])
    if variable_2 > variable:
        variable = variable_2
print(variable)
