import math
def koogi_hind(nimi, moot):
    lopp = 0
    if nimi == "šokolaadikook":
        lopp = round(math.pi * (moot **2) * 0.06, 2)
        return lopp
    elif nimi == "ploomikook":
        lopp = round(math.pi * (moot **2) * 0.04, 2)
        return lopp
    elif nimi == "Napoleoni kook":
        lopp = round(moot * moot * 0.10, 2)
        return lopp
    else:    
        return ("Sellist kooki andmebaasist ei leitud")    

while True:
    koogi_nimi = input("Sisestage koogi nimi: ")
    if koogi_nimi == "":
        break
    koogi_moot = float(input("Sisestage koogi mõõt: "))
    print(koogi_hind(koogi_nimi, koogi_moot))