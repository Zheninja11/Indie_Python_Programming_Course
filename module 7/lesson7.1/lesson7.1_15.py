def count_letters(sentence):
    numbers_lowers_and_uppers_letters = {
        'numbers_uppercase_characters': 0,
        'numbers_lowercase_characters': 0
    }

    for letter in sentence:
        if not letter.isalpha():
            continue
        else:
            if letter.isupper():
                numbers_lowers_and_uppers_letters['numbers_uppercase_characters'] += 1
            else:
                numbers_lowers_and_uppers_letters['numbers_lowercase_characters'] += 1
    
    print(f'Количество заглавных символов: {numbers_lowers_and_uppers_letters["numbers_uppercase_characters"]}')
    print(f'Количество строчных символов: {numbers_lowers_and_uppers_letters["numbers_lowercase_characters"]}')
