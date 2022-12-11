import math

def koogi_hind(a, b):
    hind = 0
    if a == ("šokolaadikook"):
        hind = (math.pi * b ** 2 * 0.06)
        return round(hind, 2)
    elif a == ("ploomikook"):
        hind = (math.pi * b ** 2 * 0.04)
        return round(hind, 2)
    elif a == ("Napoleoni kook"):
        hind = (b * b * 0.1)
        return round(hind, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

kook = 0
suurus = 0
while True:
    kook = input("Sisestage kook: ")
    if kook == "":
        break
    suurus = float(input("Sisestage koogi suurus sentimeetrites:"))
    print("Koogi hind on:", koogi_hind(kook, suurus), " eurot")

    