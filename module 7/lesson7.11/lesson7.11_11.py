directory_phone = {}

for _ in range(int(input())):
    number_phone, name = input().split(' ')

    if name in directory_phone:
        directory_phone[name].append(number_phone)
    else:
        directory_phone[name] = [number_phone]

for _ in range(int(input())):
    request = input()
    if request in directory_phone:
        print(' '.join(sorted(directory_phone[request])))
    else:
        print('Неизвестный номер')
