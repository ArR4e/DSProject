from math import pi
def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return(round(mõõt**2*pi*0.06,2))
    elif nimi == "ploomikook":
        return(round(mõõt**2*pi*0.04,2))
    elif nimi == "Napoleoni kook":
        return(round(mõõt**2*0.1,2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    kNimi = input("Sisestage koogi nimi: ")
    if kNimi == "":
        break
    else:
        kMõõt = float(input("Sisestage koogi mõõt: "))
        print(koogi_hind(kNimi,kMõõt))