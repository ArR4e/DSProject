from math import pi
def koogi_hind(a,moot):
    if a == "šokolaadikook":
        return round(0.06 * pi * moot**2,2)
    if a == "ploomikook":
        return round(0.04 * pi * moot**2,2)
    if a == "Napoleoni kook":
        return round(0.10 * moot**2,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
a = input("Sisesta koogi nimi: ")
while True:
    if a =="":
        break
    moot = float(input("Sisesta koogi mõõt: "))
    print(round(koogi_hind(a,moot), 2))
    a = input("Sisesta koogi nimi: ")
    