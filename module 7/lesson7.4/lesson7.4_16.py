def shift_letter(letter: str | int, shift_step: str | int):
    'Функция сдвигает символ letter на shift позиций'

    letter_shift = (ord(letter.lower()) - ord('a') + shift_step) % 26 + ord('a')

    return chr(letter_shift)

def caesar_cipher(sentence: str, shift_step: int):
    'Шифр цезаря'

    caesar_cipher_list = []

    for symbol in sentence:
        if symbol in 'abcdefghijklmnopqrstuvwxyz':
            caesar_cipher_list.append(shift_letter(symbol.lower(), shift_step))
        else:
            caesar_cipher_list.append(symbol)
    
    return ''.join(caesar_cipher_list)

print(caesar_cipher('leave out all the rest', -1))
