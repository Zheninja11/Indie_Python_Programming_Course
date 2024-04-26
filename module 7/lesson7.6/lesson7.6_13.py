def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
    'Функция создает матрицу размером size*size, заполняя её числами up_fill выше главной диагонали и числами down_fill ниже'

    matrix = [[number + 1 for number in range(size)] for number in range(size)]

    for i in range(size):
        for j in range(size):
            if i > j:
                matrix[i][j] = down_fill
            elif i < j:
                matrix[i][j] = up_fill
    
    return matrix
