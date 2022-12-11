from math import pi

def koogi_hind(nimi, mõõt):
    if (nimi == 'šokolaadikook' and mõõt >= 0):
        p1 = pi * mõõt**2
        return round(float(p1*0.06), 2)
    elif (nimi == 'ploomikook' and mõõt >= 0):
        p2 = pi * mõõt**2
        return round(float(p2*0.04), 2)
    elif (nimi == 'Napoleoni kook' and mõõt >= 0):
        p3 = mõõt**2
        return round(float(p3*0.10), 2)
    else:
        raise Exception('Sellist kooki andmebaasis ei leidu!')

while True:
    nimi = input('Sisestage mis koogiga tegu on? (šokolaadikook, ploomikook, Napoleoni kook): ')
    if (nimi == ''):
        break
    mõõt = float(input('Mis on koogi raadius/külg?: '))
    if (koogi_hind(nimi, mõõt > 0)):
        print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot.")
    else:
        pass
