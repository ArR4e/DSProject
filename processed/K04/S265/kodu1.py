from math import pi

def koogi_hind(nimi,moot):
    if nimi == 'šokolaadikook':
        return round(0.06*moot**2*pi,2)
    elif nimi == 'ploomikook':
        return round(0.04*moot**2*pi,2)
    elif nimi == 'Napoleoni kook':
        return round(0.10*moot**2,2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud')

while True:
    nimi = input('nimi: ')
    if nimi == '':
        break
    moot = input('suurus: ')
    print(koogi_hind(nimi,float(moot)))