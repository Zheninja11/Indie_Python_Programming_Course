def is_sorted_descending(lst):
    
    return all(lst[i] > lst[i+1] for i in range(len(lst)-1))

input_list = list(map(int, input().split()))

result = is_sorted_descending(input_list)

print(result)
