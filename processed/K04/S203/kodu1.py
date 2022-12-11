import math

def koogi_hind(nimi, mõõt):
    if nimi != 'šokolaadikook' and nimi != 'ploomikook' and nimi != 'Napoleoni kook':
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    if nimi == 'šokolaadikook':
        moot = float(mõõt)
        hind = math.pi * (moot ** 2) * 0.06
        hind_lopp = round(hind, 2)
        return hind_lopp
    elif nimi == 'ploomikook':
        moot = float(mõõt)
        hind = math.pi * (moot ** 2) * 0.04
        hind_lopp = round(hind, 2)
        return hind_lopp
    elif nimi == 'Napoleoni kook':
        moot = float(mõõt)
        hind = moot * moot * 0.10
        hind_lopp = round(hind, 2)
        return hind_lopp
    
while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == '':
        break
    else:
        mõõt = input("Sisesta koogi mõõt: ")
        hind = koogi_hind(nimi, mõõt)
        print("Koogi hind on: ", hind)