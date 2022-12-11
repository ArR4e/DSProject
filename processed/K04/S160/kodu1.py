from math import pi
from math import *

def koogi_hind(nimi, mõõt):
    valem_soko = round(0.06 * mõõt**2 * pi, 2)
    valem_ploom = round(0.04 * mõõt**2 * pi, 2)
    valem_napol = round(0.10 * mõõt**2, 2)
    if nimi == "ploomikook":
        hind = round(valem_ploom, 2)
        return hind
    
    elif nimi == "Napoleoni kook":
        hind = round(valem_napol, 2)
        return hind
    
    elif nimi == "šokolaadikook":
        hind = round(valem_soko, 2)
        return hind
    else:
        raise Exception("Poes pole sellist kooki!")
        
while True:
    nimi = input("Sisesta koogivalik: ")
    if nimi == "":
        break
    
    mõõt =float(input("Sisesta koogi parameeter: "))
        
    hind = koogi_hind(nimi, mõõt)
    print(nimi + " maksab " + str(hind) + "€")
