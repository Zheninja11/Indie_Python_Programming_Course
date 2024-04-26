def print_goods(*args):
    counter = 0

    for arg in args:
        if isinstance(arg, str):
            if arg != '':
                counter += 1
                print(f'{counter}. {arg}')
        else:
            continue
    
    if counter == 0:
        print('Нет товаров')
