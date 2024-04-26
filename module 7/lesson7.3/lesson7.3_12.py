def first_unique_char(sentence):
    unique_values_string = []

    for letter in sentence:
        if sentence.count(letter) == 1:
            unique_values_string.append(sentence.index(letter))
        else:
            continue
    
    if len(unique_values_string) == len(sentence):
        return unique_values_string[0]
    elif len(unique_values_string) >= 1:
        return unique_values_string[0]
    else:
        return - 1
