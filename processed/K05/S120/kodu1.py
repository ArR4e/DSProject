
username = input('Sisestage kasutajanimi: ')

invalid_password = True
while invalid_password:
    password = input('Sisestage parool: ')
    password_confirm = input('Sisestage parool uuesti: ')

    if password == password_confirm:
        if len(password) >= 8:
            if len(password) != len(''.join(letter for letter in password if letter not in '0123456789')):
                password = password[::-1]
                invalid_password = False
            else:
                print('Parool peab sisaldama numbreid.')
        else:
            print('Parool peab olema vähemalt 8 tähemärki pikk.')
    else:
        print('Sisestatud paroolid ei kattu.')
    print()

with open('users.txt', 'w') as f:
    f.write(f'{username}:{password}')