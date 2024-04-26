def create_file_with_numbers(n):
    file = open(f'range_{n}.txt', 'x')
    for i in range(n):
        file.write( str(i + 1) + '\n')
    file.close()
