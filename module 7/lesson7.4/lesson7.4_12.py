from typing import Optional

def first_repeated_word(row: str):
    'Находит первый дубль в строке'

    row = row.split(' ')
    dublicate: Optional[list] = []

    for letter in row:
        if letter not in dublicate:
            dublicate.append(letter)
        else:
            return letter
            break
    
    if len(row) == len(dublicate):
        dublicate = None
        return None
