from math import pi

def koogi_hind(nimi, moot):
    if nimi == "šokolaadikook":
        S = pi*moot**2
        return round((S*0.06), 2)
    elif nimi == "ploomikook":
        S = pi*moot**2
        return round((S*0.04), 2)
    elif nimi == "Napoleoni kook":
        S = moot**2
        return round((S*0.10), 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    kooginimi = input("Sisestage koogi nimi: ")
    if kooginimi == "":
        break
    else:
        koogimoot = float(input("Sisestage koogi mõõt: "))
        print(koogi_hind(kooginimi, koogimoot))