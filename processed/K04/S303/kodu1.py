from math import pi

class CakeNotFoundException(Exception):
    def __init__(self):
        super().__init__('Sellist kooki andmebaasist ei leitud')
        

def koogi_hind(nimi, mõõt):
    if nimi.lower() == 'šokolaadikook':
        pind = pi * mõõt**2
        return round(pind * .06, 2)
    elif nimi.lower() == 'ploomikook':
        pind = pi * mõõt**2
        return round(pind * .04, 2)
    elif nimi.lower() == 'napoleoni kook':
        pind = mõõt**2
        return round(pind * .1, 2)
    else:
        raise CakeNotFoundException()

while True:
    nimi = input('Sisestage koogi nimi: ')
    if not nimi: break
    mõõt = float(input('Sisestage koogi mõõt: '))
    if mõõt <= 0:
        print('Mõõt peab olem rohkem kui 0')
        exit()
    print(f'Koogi hind on {koogi_hind(nimi, mõõt)}')
