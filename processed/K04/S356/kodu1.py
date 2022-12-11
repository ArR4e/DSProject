from math import pi

def koogi_hind(nimi,moot):
    
    if nimi != 'šokolaadikook' and nimi != 'ploomikook' and nimi != 'Napoleoni kook':
        raise Exception("Sellist kooki andmebaasist ei leitud.")
        
    elif nimi != 'Napoleoni kook' and nimi != 'ploomikook':
        return round(0.06 * (pi * moot**2),2)
    elif nimi != 'šokolaadikook' and nimi != 'ploomikook':
        return round(0.10 * (moot**2),2)
    elif nimi != 'šokolaadikook' and nimi != 'Napoleoni kook':
        return round(0.04 * (pi * moot**2),2)


while True:
    k1 = input("Sisesta koogi nimi: ")
    if k1 == '':
        break
    else:
        m1 = float(input("Sisesta koogi mõõt: "))
        hind = koogi_hind(k1,m1)
        print(k1, "maksab " + str(hind) + " €.")
