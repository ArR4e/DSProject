
from math import pi

def koogi_hind(nimi,mõõt):
    if nimi == "šokolaadikook":
        return round(0.06*float(mõõt)**2*pi,2)
    elif nimi == "ploomikook":
        return round(0.04*float(mõõt)**2*pi,2)
    elif nimi == "Napoleoni kook":
        return round(0.10*float(mõõt)**2,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
        
while True:
    nimi = input("Vali pagarikoja kook: ")
    if nimi == "":
        break
    mõõt = input("Vali koogi suurus: ")
    print(koogi_hind(nimi,mõõt))

    
    