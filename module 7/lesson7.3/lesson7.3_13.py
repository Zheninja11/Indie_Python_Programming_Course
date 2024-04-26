def format_name_list(dict_of_names):
    if not dict_of_names:
        return ''
    
    names = [value['name'] for value in dict_of_names]
    
    if len(names) == 2:
        return names[0] + ' и ' + names[1]
    elif len(names) == 1:
        return names[0]
    elif len(names) > 2:
        return ', '.join(names[:-1]) + ' и ' + names[-1]
