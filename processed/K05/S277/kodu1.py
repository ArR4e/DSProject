nimi = input('Sisestage kasutajanimi: ')
contin = True

while contin is True:
    parool = input('Sisestage parool: ')
    parool2 = input('Sisestage parool teist korda: ')
    if parool != parool2:
        print('Paroolid peavad samad olema')
    elif parool == parool2:
        if len(parool) < 8:
            print('Parool peab vähemalt 8 tähemärki olema')
        elif len(parool) >= 8:
            if parool.isalpha() is True or parool.isdigit() is True:
                print('Parool peab sisaldama tähti ja numbreid')
            else:
                n = 0
                krypt = ''
                for taht in parool:
                    a = list(parool)
                    krypt += ''.join(a[-1 - n])
                    n += 1
                    contin = False
                    
f = open('users.txt', 'w')
f.write(':'.join([nimi, krypt]))
f.close()
