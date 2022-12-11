import math
def koogi_hind(nimi, mõõt):
    if nimi == 'šokolaadikook':
        return round(float(math.pi*mõõt**2*0.06), 2)
    elif nimi == 'ploomikook':
        return round(float(math.pi*mõõt**2*0.04), 2)
    elif nimi == 'Napoleoni kook':
        return round(float(mõõt**2)*0.1, 2)
    else:
        raise ValueError('Sellist kooki andmebaasist ei leitud.')
        

while True:
    nimi = input('Sisesta koogi nimi: ')
    if nimi == '':
        break
    mõõt = float(input('Sisesta koogi mõõt: '))
    x = koogi_hind(nimi, mõõt)
    print(nimi, 'maksab', x, 'eurot.')
    