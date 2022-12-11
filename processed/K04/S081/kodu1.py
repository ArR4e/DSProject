import math

def koogi_hind(nimi, mõõt):
    if (nimi).upper() == ('šokolaadikook').upper():
        hind = round(((mõõt**2) * (math.pi)) * 0.06, 2)
    elif (nimi).upper() == ('ploomikook').upper():
        hind = round(((mõõt**2) * (math.pi)) * 0.04, 2)
    elif (nimi).upper() == ('napoleoni kook').upper():
        hind = round((mõõt**2) * 0.1, 2)    
    else:
        raise Exception('Sellist kooki pole')
    return hind

while True:
    nimi = input('Sisestage koogi nimi: ')
    if nimi == '':
        break
    else:
        mõõt = float(input('Sisestage koogi mõõt: '))
        hind = koogi_hind(nimi, mõõt)
        print('Koogi hind on', str(hind)+'€')

