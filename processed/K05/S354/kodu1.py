kasutajanimi = input('Sisestage oma kasutajanimi: ')
i = 0
while i < 4:
    parool_1 = (input('Sisestage oma parool ,esimene kord: '))
    parool_2 = (input('Sisestage oma parool ,trine kord: '))
    if parool_1 == parool_2:
        i += 1
        if len(parool_1) >= 8:
            i += 1
            if parool_1.isdecimal():
                i = 0
                print('try again')
                continue
            if parool_1.isalpha():
                i = 0
                print('try again')
            else:
                i += 1
                break
        else:
            i = 0
            print('try again')
    else:
        i = 0
        print('try again')
summa = ''
t = len(parool_1) - 1

while t >= 0:
    summa = summa + parool_1[t] 
    t -= 1

f = open('users.txt', 'w')
f.write(kasutajanimi + '\n')
f.write(summa + '\n')
f.close()
