pair_number_n, pair_number_m = map(int, input().split())

count_pair_number = 0

for a in range(pair_number_n + 1):
    for b in range(pair_number_m + 1):
        if a ** 2 + b == pair_number_n and a + b ** 2 == pair_number_m:
            count_pair_number += 1
print(count_pair_number)
