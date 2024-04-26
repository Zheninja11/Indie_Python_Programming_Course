def file_n_lines(name: str, n: int):
    f = open(name, 'r', encoding = 'utf-8')
    for i in range(n):
        print(f.readline(), end = '')
    f.close()
