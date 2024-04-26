with open('words.txt') as f:

    spis = []

    for i in f.readlines():
        a = i.replace('\n', '')
        a = a.upper()
        if a[-2:] == 'ЕЯ' and a not in spis:
            spis.append(a)

    print(*sorted(spis, key=lambda x: len(x)), sep='\n')
