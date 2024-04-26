def get_body_mass_index(body_weight, height_in_cm):
    index = body_weight / ((height_in_cm / 100) ** 2)
    if index < 18.5:
        print('Недостаточная масса тела')
    elif index > 25.0:
        print('Избыточная масса тела')
    else:
        print('Норма')
