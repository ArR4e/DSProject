from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == 'šokolaadikook':
        return round(pi * mõõt**2 * 0.06, 2)
    elif nimi == 'ploomikook':
        return round(pi * mõõt**2 * 0.04, 2)
    elif nimi == 'Napoleoni kook':
        return round(mõõt**2 * 0.10, 2)
    else:
        raise ValueError('Sellist kooki andmebaasist ei leitud')
        
while True:
    nimi = input('Sisestage koogi nimi: ')
    if nimi == '':
        break
    mõõt = float(input('Sisestage koogi mõõt: '))
    print('Koogi hind on', koogi_hind(nimi, mõõt), 'eurot.')