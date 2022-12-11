#alustasin 20.09.2021 (14:00)
from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        pindala = pi * mõõt**2
        return round(0.06 * pindala, 2)
    elif nimi == "ploomikook":
        pindala = pi * mõõt**2
        return round(0.04 * pindala, 2)
    elif nimi == "Napoleoni kook":
        pindala = mõõt**2
        return round(0.10 * pindala, 2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud.')

while True:
    nimi = input('Sisestage koogi nimi: ')
    if nimi == '':
        break
    mõõt = float(input('Sisestage koogi mõõt: '))
    print('Koogi hind on', koogi_hind(nimi, mõõt), 'eurot.')   