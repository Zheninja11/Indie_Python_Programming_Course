def shift_letter(letter: str | int, ascii_code: str | int):
    'Функция сдвигает символ letter на shift позиций'

    letter_shift = (ord(letter.lower()) - ord('a') + ascii_code) % 26 + ord('a')

    return chr(letter_shift)
