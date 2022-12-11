from math import pi

def koogi_hind(a, b):
    if a == "šokolaadikook":
        hind = 0.06
        maksumus = round((hind*pi*b**2), 2)
    elif a == "ploomikook":
        hind = 0.04
        maksumus = round((hind*pi*b**2), 2)
    elif a == "Napoleoni kook":
        hind = 0.10
        maksumus = round((hind*b**2), 2)
    else:
        raise Exception ("Sellist kooki andmebaasist ei leitud")
    return maksumus

while True:
    a = input("Koogi nimi: ")
    if a == "":
        break
    b = float(input("Koogi mõõt (cm, šokolaadi- ja ploomikoogil raadius, Napoleoni koogil ruudu külje pikkus: "))
    print(koogi_hind(a, b))

    
