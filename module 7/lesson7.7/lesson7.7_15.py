def info_kwargs(**kwargs):
    'Функция выводить именованные аргументы в каждой новой строке в виде пары "ключ: значение"'

    for key, value in sorted(kwargs.items()):
        print(f"{key} = {value}")
