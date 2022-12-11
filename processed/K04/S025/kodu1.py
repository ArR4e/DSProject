from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == 'ploomikook' or nimi == 'Ploomikook':
        pindala = pi * mõõt ** 2
        return round((pindala * 0.04), 2)
    elif nimi == 'Napoleoni kook' or nimi == 'napoleoni kook':
        pindala = mõõt ** 2
        return round((pindala * 0.10), 2)
    elif nimi == 'Šokolaadikook' or nimi == 'šokolaadikook':
        pindala = pi * mõõt ** 2
        return round((pindala * 0.06), 2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud')

while True:
    nimi = str(input('Sisestage koogi nimi '))
    if nimi == '':
        break
    mõõt = float(input('Sisestage koogi mõõt '))
    print(koogi_hind(nimi, mõõt))
