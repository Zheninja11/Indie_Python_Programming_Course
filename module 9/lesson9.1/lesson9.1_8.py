from string import punctuation

def remove_punctuations(word):

    for punct in punctuation:
        if punct in word:
            word = word.replace(punct, "")

    return word

def longest_word_in_file(file_name):

    file = open(file_name, "r", encoding="utf-8")
    max_word = ""

    for line in file:
        words = line.split()
        for word in words:
            word_without_punct = remove_punctuations(word)
            if len(word_without_punct) >= len(max_word):
                max_word = word_without_punct

    return max_word
