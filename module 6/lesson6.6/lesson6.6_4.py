number = int(input())
login_store = {}
counter = 0

for i in range(number):
    login = input()
    if login not in login_store:
        login_store[login] = 0
        print('OK')
    else:
        login_store[login] += 1
        login = login + str(login_store[login])
        print(login)
        login_store[login] = 0
