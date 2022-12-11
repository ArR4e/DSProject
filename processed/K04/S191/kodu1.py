from math import pi

def koogi_hind(nimi,moot):
    x=0
    if nimi=='šokolaadikook' or nimi=='ploomikook':
        if nimi=='šokolaadikook':
            x=round((pi*moot**2)*0.06,2)
            return x
        else:
            x=round((pi*moot**2)*0.04,2)
            return x
    elif nimi=='Napoleoni kook':
        x=round((moot**2)*0.10,2)
        return x
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud\n')

while True:
    nimi=input('Millist kooki soovite? (tühi sisend peatab programmi) ')
    if nimi=='':
        break
    moot=float(input('Mis mõõtudega kooki soovite? (cm) '))
    print('Selline kook maksab',koogi_hind(nimi,moot),'€\n')
