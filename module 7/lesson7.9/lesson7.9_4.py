def quick_sort(s):
    if len(s) <= 1:
        return s
    
    n = s.pop(len(s)//2)
    less = [i for i in s if i <= n]
    more = [i for i in s if i > n]

    return quick_sort(less) + [n] + quick_sort(more)
