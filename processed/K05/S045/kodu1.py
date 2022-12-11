def numbrid_sõna_check(sõna):
    return not sõna.isalpha() and not sõna.isdigit()

def reverse_string(sõna):
    tagurpidi = []
    tagurpidi[:0] = sõna
    tagurpidi.reverse()
    return "".join(tagurpidi)
    

parool_puudu = True
kasutajanimi = input('Sisesta kasutajanimi: ')
while parool_puudu:
    parool_1 = input('Sisesta parool: ')
    parool_2 = input('Sisesta parool uuesti: ')
    if parool_1 == parool_2 and len(parool_1) >= 8 and numbrid_sõna_check(parool_1):
        parool_puudu = False
        with open('users.txt', 'w') as file:
            file.write(f'{kasutajanimi}:{reverse_string(parool_1)}')
    else:
        if parool_1 != parool_2: 
            print('Paroolid olid erinevad. Proovi uuesti.')
        elif len(parool_1) < 8:
            print('Parool peab olema vähemalt 8 tähemarki. Proovi uuesti.')
        elif not numbrid_sõna_check(parool_1):
            print('Parool peab sisaldama tähti ja numbreid. Proovi uuesti.')
