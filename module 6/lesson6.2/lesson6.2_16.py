n = int(input())
numbers = []

for i in range(n, n ** 2 + 1):
    if i % 2 != 0:
        numbers.append(i)

numbers = tuple(numbers)

print(numbers)
