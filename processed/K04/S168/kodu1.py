from math import pi
def koogi_hind(nimi, mõõtmed):
    if nimi == "šokolaadikook":
        hind = 0.06 * mõõtmed**2 * pi
    elif nimi == "ploomikook":
        hind = 0.04 * mõõtmed**2 * pi
    elif nimi == "Napoleoni kook":
        hind = 0.1 * mõõtmed**2
    return hind
        
while True:
    try:
        nimi = str(input("Sisesta koogi nimi (kas šokolaadikook, ploomikook või Napoleoni kook): "))
        mõõtmed = str(input("Sisesta koogi mõõtmed: "))
        if nimi == "" or mõõtmed == "":
            break
        if nimi != "šokolaadikook" and nimi != "ploomikook" and nimi != "Napoleoni kook":
            raise Exception
        mõõtmed = float(mõõtmed)
        hind = koogi_hind(nimi, mõõtmed)
        print("Koogi hind on", round(hind, 2), "eurot.")
    except:
        print("Sellist kooki andmebaasist ei leitud.")

