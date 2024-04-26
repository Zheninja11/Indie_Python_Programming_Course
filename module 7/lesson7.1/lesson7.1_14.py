def check_password(password):
    password_settings = {'count_numbers': 0, 
                         'capitalizatio_rate': 0, 
                         'number_special_characters': 0}
    
    special_characters = ['!', '@', '#', '$', '%', '*']

    if len(password) >= 10:
        for symbole in password:
            if symbole.isdigit():
                password_settings['count_numbers'] += 1
            elif symbole.isupper():
                password_settings['capitalizatio_rate'] += 1
            elif symbole in special_characters:
                password_settings['number_special_characters'] += 1
        if password_settings['capitalizatio_rate'] >= 1 and password_settings['count_numbers'] >= 3 and password_settings['number_special_characters'] >= 1:
            print('Perfect password')
        else:
            print('Easy peasy')
    else:
        print('Easy peasy')
