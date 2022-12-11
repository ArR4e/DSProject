from math import pi

def koogi_hind(nimi, moot):
    if nimi == "šokolaadikook":
        return round(((pi*moot*moot)*0.06), 2)
    if nimi == "ploomikook":
        return round(((pi*moot*moot)*0.04), 2)
    if nimi == "Napoleoni kook":
        return round(((moot*moot)*0.1), 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    n = input("Sisesta koogi nimi: ")
    if n == "":
        break
    m = float(input("Sisesta koogi mõõt: "))
    print("Teie",n,"läheb maksma",koogi_hind(n, m),"€.")
