from math import pi

def koogi_hind(nimi, moot):
    if nimi == "šokolaadikook":
        return round(0.06*(pi * moot**2), 2)
    elif nimi == "ploomikook":
        return round(0.04*(pi * moot**2), 2)
    elif nimi == "Napoleoni kook":
        return round(0.10*(moot**2), 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    nimi = input("Sisesta koogi nimi (valikuteks šokolaadikook, ploomikook või Napoleoni kook): ")
    if nimi == "":
        break
    moot = float(input("Sisesta koogi mõõtmed: "))
    print("Koogi hinnaks on " + str(koogi_hind(nimi, moot)))