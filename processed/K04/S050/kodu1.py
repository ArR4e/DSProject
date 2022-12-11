from math import pi



def koogi_hind(knimi,m):
    if knimi == 'šokolaadikook':
        return round(pi*(m**2)*0.06,2)
    elif knimi=='ploomikook':
        return round(pi*(m**2)*0.04,2)
    elif knimi== 'Napoleoni kook':
        return round(m**2*0.10,2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud.')
    
while True:
    knimi= input('Palun sisesta koogi nimi: ')
    if knimi == '':
        break
    m=float(input('Palun sisesta koogi mõõt: '))
    print(koogi_hind(knimi,m))