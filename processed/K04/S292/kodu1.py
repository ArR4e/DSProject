import math

def koogi_hind(nimi, suurus):
    if nimi == "šokolaadikook":
        pindala =  math.pi * suurus * suurus
        return round(pindala*0.06, 2)
    elif nimi == "ploomikook":
        pindala =  math.pi * suurus * suurus
        return round(pindala*0.04, 2)
    elif nimi == "Napoleoni kook":
        pindala =  suurus * suurus
        return round(pindala*0.1, 2)
    else:
        raise Exception("„Sellist kooki andmebaasist ei leitud”")
       
while True:
    nimi = input("Mis on koogi nimi?: ")
    if nimi == "":
        break
    suurus = float(input("Mis on koogi suurus?: "))
    print("Koogi hind on", koogi_hind(nimi, suurus))