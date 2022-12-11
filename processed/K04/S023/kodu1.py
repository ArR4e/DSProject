import math


def koogi_hind(nimi,r):
    r = float(r)
    if nimi == "ploomikook":
        koogihind = round(((math.pi * r * r)*0.04),2)
        return print(koogihind)
    if nimi == "šokolaadikook":
        koogihind = round(((math.pi * r * r)*0.06),2)
        return print(koogihind)
    if nimi == "Napoleoni kook":
        koogihind = round(((r * r)*0.10),2)
        return print(koogihind)
    else:
        return print("Sellist kooki andmebaasist ei leitud.")
nimi = input("Sisestage koogi nimi:")
r = input("Sisestage koogi raadius: ")
koogi_hind(nimi,r)