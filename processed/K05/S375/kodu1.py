k_nimi = input('Sisestage oma kasutajanimi: ')

a = 0
x = 0
y = 0
while a != 1:
    parool1 = input('Sisestage oma parool: ')
    parool2 = input('kinnitage oma parool: ')
    if parool1 == parool2:
        if len(parool1) >= 8:
            for el in parool1:
                if el.isalpha() == True:
                    x += 1
                elif el.isnumeric() == True:
                    y += 1
            if  x >= 1 and y >= 1:
                a += 1
            else:
                print('Veateade: Teie paroolis ei ole tähti või numbreid.')
        else:
            print('Veateade: Teie parool on liiga lühike')
    else:
        print('Veateade: Teie sisestatud paroolid ei klapi üksteisega.')
parool1 = parool1 [:: -1]
fail = open('users.txt', 'w', encoding='UTF-8')
fail.write(k_nimi)
fail.write(':')
fail.write(parool1)
fail.close()

                    
            
