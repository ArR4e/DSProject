from math import pi
def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi == "šokolaadikook":
        koogi_hind = mõõt**2*pi*0.06
        print("šokolaadikoogi hind on", round(koogi_hind, 2))
    elif koogi_nimi == "ploomikook":
        koogi_hind = mõõt**2*pi*0.04
        print("ploomikoogi hind on", round(koogi_hind, 2))
    elif koogi_nimi == "Napoleoni kook":
        koogi_hind = mõõt**2*0.1
        print("Napoleoni koogi hind on", round(koogi_hind, 2))
    else:
        print("Sellist kooki andmebaasist ei leitud")
while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    mõõt = float(input("Sisesta koogi mõõde: "))
    koogi_hind(koogi_nimi, mõõt)
    if koogi_nimi == "":
        break

    
    



