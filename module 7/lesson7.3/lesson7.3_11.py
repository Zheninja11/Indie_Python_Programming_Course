def find_duplicate(numbers: list):
    dublicates = []

    for number in numbers:
        if number in dublicates:
            continue
        if numbers.count(number) > 1: 
            dublicates.append(number)
    
    return dublicates
