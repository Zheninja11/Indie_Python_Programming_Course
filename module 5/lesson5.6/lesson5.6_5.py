n = int(input())
count = 0

for i in range(n + 1, 2 * n):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime and i > 1:
        count += 1
print(count)
