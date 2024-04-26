number = int(input())
i = 1
sum_digit = 0
while i <= number:
    if number % i == 0:
        sum_digit = sum_digit + i
    i += 1
print(sum_digit)
