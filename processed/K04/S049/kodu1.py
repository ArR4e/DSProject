koogi_nimi = input("Sisestage koogi nimi: ")
koogi_mõõt = float(input("Sisestage koogi mõõt: "))

from math import pi

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        return(0.06 * (koogi_mõõt ** 2 * pi))
    elif koogi_nimi == "ploomikook":
        return(0.04 * (koogi_mõõt ** 2 * pi))
    elif koogi_nimi == "Napoleoni kook":
        return(0.10 * (koogi_mõõt ** 2))
    else:
        raise Exeption("Sellist kooki andmebaasist ei leitud.")
    print("Koogi maksumus on:" + (koogi_nimi, koogi_mõõt))







'''def koogi_hind(koogi_nimi, koogi_mõõt):
    šokolaadikook = 0.06 * (koogi_mõõt ** 2 * pi)
    return šokolaadikook

print("Koogi hind on: " + str(koogi_hind(koogi_nimi)))'''

