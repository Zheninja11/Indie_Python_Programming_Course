def create_dict():
    counter = 0
    dict_func = {}

    def inner_func(row):
        nonlocal counter
        nonlocal dict_func
        counter += 1
        dict_func[counter] = row
        return dict_func
    
    return inner_func
