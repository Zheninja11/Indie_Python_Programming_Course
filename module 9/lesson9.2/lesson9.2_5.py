with open('lorem.txt') as f:

    words = {}
    
    for i in f.readlines():
        for j in i.split():
            a = j.replace('\n', '')
            if a.upper() in words:
                words[a.upper()] += 1
            else:
                words[a.upper()] = 1
