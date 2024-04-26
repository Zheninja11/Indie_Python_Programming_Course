def sum_num(row=str):
    numbers = []
    for symbole in row:
        if symbole.isdigit():
            numbers.append(int(symbole))
    
    print(sum(numbers))
