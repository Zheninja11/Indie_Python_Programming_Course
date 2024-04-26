def calculate(x:float, y:float, operation: str = 'a'):
    def addition(x, y):
        print(float(x + y))
    
    def subtraction(x, y):
        print(float(x - y))
    
    def divison(x, y):
        if y != 0:
            print(float(x / y))
        else:
            print('На ноль делить нельзя!')
    
    def multiplication(x, y):
        print(float(x * y))

    if operation == 'a':
        addition(x, y)
    elif operation == 's':
        subtraction(x, y)
    elif operation == 'd':
        divison(x, y)
    elif operation == 'm':
        multiplication(x, y)
    else:
        print('Ошибка. Данной операции не существует')
