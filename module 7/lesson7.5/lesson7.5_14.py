def get_word_indices(strings: list[str]) -> dict:
    dct = {j: 0 for i in strings for j in i.lower().split()}
    
    for i in dct:
        z = []
        for j in range(len(strings)):
            if i in strings[j].lower():
                z.append(j)  
        dct[i] = (z)
        
    return dct
