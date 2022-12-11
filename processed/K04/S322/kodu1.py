from math import pi
def koogi_hind(nimi, suurus):
    if nimi == "šokolaadikook":
        return round((pi * suurus ** 2)  * 0.06, 2)
    elif nimi == "ploomikook":
        return round((pi * suurus ** 2) * 0.04, 2)
    elif nimi == "Napoleoni kook":
        return round(suurus**2 * 0.1, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    kook = input("Sisesta koogi nimi: ")
    if kook == "":
        break
    mootmed = float(input("Sisestage raadius/külje pikkus (cm): "))
    print(f"Koogi hind on {koogi_hind(kook, mootmed)}€")