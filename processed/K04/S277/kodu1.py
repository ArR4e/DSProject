sokhind = 0.06
plohind = 0.04
naphind = 0.10
from math import pi

def koogi_hind(nimi, moot):
    if nimi == 'šokolaadikook':
        maksumus = round(sokhind * (pi * moot ** 2), 2)
        return maksumus
    elif nimi == 'ploomikook':
        maksumus = round(plohind * (pi * moot ** 2), 2)
        return maksumus
    elif nimi == 'Napoleoni kook':
        maksumus = round(naphind * (moot ** 2), 2)
        return maksumus
    else:
        raise Exception('Sellist kooki andmebaasis ei ole')
        
nimi = input('Sisestage otsitava koogi nimi: ')
moot = float(input('Sisestage soovitava koogi moot: '))

while nimi != '':
    print('Koogi hind on', koogi_hind(nimi, moot), 'eurot.')
    nimi = input('Sisestage otsitava koogi nimi: ')
    if nimi == '':
        break
    moot = float(input('Sisestage soovitava koogi moot: '))
