def list_sum_recursive(a: list) -> int:
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    return a[0] + list_sum_recursive(a[1:])
