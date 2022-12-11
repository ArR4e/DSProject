# Pagarikoja kassaaparaat

from math import pi
def koogi_hind(kook, mõõt):
    if kook.lower() == "šokolaadikook":
        #S = pi*r**2
        return round(pi*mõõt**2*0.06, 2)
    elif kook.lower() == "ploomikook":
        #S = pi*r**2
        return round(pi*mõõt**2*0.04, 2)
    elif kook.lower() == "napoleoni kook":
        #S = r**2
        return round(mõõt**2*0.1, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    try:
        koogi_nimi = input("Sisestage koogi nimi: ")
        if koogi_nimi == "":
            break
        koogi_mõõt = float(input("Sisestage koogi mõõtmed: "))
        print(koogi_hind(koogi_nimi, koogi_mõõt))
    except:
        print("Sellist kooki andmebaasist ei leitud")