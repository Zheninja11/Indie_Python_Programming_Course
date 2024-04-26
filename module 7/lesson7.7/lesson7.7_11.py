def only_one_positive(*args) -> bool:
    if not args:
        return False
    
    result = 0

    for number in args:
        if number > 0:
            result += 1
        else:
            continue
    
    if result == 1:
        return True
    elif result > 1:
        return False
    else:
        return False
