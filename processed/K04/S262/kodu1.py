from math import *
def koogi_hind(x,y):
    if x == "šokolaadikook":
        return(round((0.06*(pi * (y**2))),2))
    elif x == "ploomikook":
        return(round((0.04*(pi * (y**2))),2))
    elif x == "Napoleoni kook":
        return(round((0.1*(y**2)),2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
kook = "a"
suurus = "b"

while True:
    kook = input("Sisestage koogi nimi ")
    if kook == "":
        break
    suurus = float(input("Sisestage koogi mõõt "))
    print("Koogi hind on", str(koogi_hind(kook,suurus)) + "€")