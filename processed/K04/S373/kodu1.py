from math import pi
def koogi_hind(a, b):
    if a == "šokolaadikook":
        return round(((pi*b*b)*0.06), 2)
    if a == "ploomikook":
        return round(((pi*b*b)*0.04), 2)
    if a == "Napoleoni kook":
        return round(((pi*b*b)*0.10), 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    kook = input("Sisesta koogi nimi: ")
    if kook == "":
        break
    mõõt = float(input("Sisesta koogi mõõt: "))
    print("Teie koogi maksumus on ", koogi_hind(kook, mõõt), " eurot.")
    
            