nimi = str(input('Kasutajanimi:'))
parool1 = ''
parool2 = 'a'

def sisaldabNumbridJaTahed(sone):
    on_taht = False
    on_arv = False
    for i in sone:
        if i.isalpha():
            on_taht = True
        elif i.isnumeric():
            on_arv = True
        if on_taht and on_arv:
            return True
    return False

def veaTuvastus(parool, parool_2):
    if parool != parool_2:
        print('parool1id ei olnud ühesugused. Proovige uuesti.')
        return False
    if len(parool) < 8:
        print('parool1 peab sisaldama vähemalt 8 tähemärki. Proovige uuesti')
        return False
    if sisaldabNumbridJaTahed(parool) == False:
        print('parool1 peab sisaldama numbreid ja tähti. Proovige uuesti.')
        return False
    return True

def kirjuta(write_parool):
    with open('users.txt', 'a') as ava_fail:
        ava_fail.write(nimi)
        ava_fail.write(':')
        ava_fail.write(write_parool)
        ava_fail.write('\n')

sisendParool1 = str(input('parool1: '))
sisendParool2 = str(input('parool1 uuesti: '))

while veaTuvastus(sisendParool1, sisendParool2) is False:
    sisendParool1 = str(input('parool1: '))
    sisendParool2 = str(input('parool1 uuesti: '))

encryption = sisendParool1 [::-1]
kirjuta(encryption)
