def create_actor(name='Райан', surname='Рейнольдс', age=46, **kwargs):
    d = dict()
    
    d.setdefault('name', name)
    d.setdefault('surname', surname)
    d.setdefault('age', age)
    
    for key, value in kwargs.items():
        d.setdefault(key, value)
    
    return d
