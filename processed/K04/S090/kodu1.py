import math

def koogi_hind(nimi, moot):
    if nimi == "šokolaadikook":
        return round((0.06 * (math.pi * moot**2)),2)
    if nimi == "ploomikook":
        return round((0.04 * (math.pi * moot**2)),2)
    if nimi == "Napoleoni kook":
        return round((0.1 * moot**2),2)
    if not nimi == "šokolaadikook" or "ploomikook" or "Napoleoni kook":
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    kook = input("Palun sisestage koogi nimi: ")
    if kook == "":
        break
    suurus = float(input("Palun sisestage koogi suurus: "))
    a = koogi_hind(kook, suurus)
    print(a)
