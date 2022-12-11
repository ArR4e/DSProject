import math


def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi == "šokolaadikook":
        pindala = math.pi * mõõt * mõõt
        hind = pindala * 0.06
    elif koogi_nimi == 'ploomikook':
        pindala = math.pi * mõõt * mõõt
        hind = pindala * 0.04
    elif koogi_nimi == "Napoleoni kook":
        pindala = mõõt * mõõt
        hind = pindala * 0.10
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")  
    return(round(hind, 2))    
        

while True:
    koogi_nimi = str(input('Sisesta koogi nimi: '))
    if koogi_nimi == "":
       break
    else:
        mõõt = float(input('Sisesta koogi mõõt (raadius) sentimeetrites: '))
        koogi_hind(koogi_nimi, mõõt)
        print(koogi_hind(koogi_nimi, mõõt))