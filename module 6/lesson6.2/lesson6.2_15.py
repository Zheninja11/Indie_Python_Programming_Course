a = int(input())
b = int(input())
numbers = []

for i in range(a, b + 1):
    numbers.append(i)

numbers = tuple(numbers)

print(numbers)
