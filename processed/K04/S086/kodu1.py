#Pagaritöökoja kassaaparaat
#šokolaadikook (0,06 €/cm2), ploomikook (0,04 €/cm2) ja Napoleoni kook (0,10 €/cm2)

from math import pi

def koogi_hind(nimi, mõõt):
    if nimi.lower() == "šokolaadikook":
        return round(mõõt**2*pi*0.06, 2)
    elif nimi.lower() == "ploomikook":
        return round(mõõt**2*pi*0.04, 2)
    elif nimi.lower() == "napoleoni kook":
        return round(mõõt**2*0.10, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")

while True:
    nimi_sisse = input("Palun sisesta koogi nimi: (Vajuta Enter, et väljuda) ")
    if nimi_sisse == "":
        break
    mõõt_sisse = float(input("Palun sisesta koogi mõõt: "))
    print(koogi_hind(nimi_sisse, mõõt_sisse))