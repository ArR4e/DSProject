import math

def koogi_hind(n, m):
    if n == "šokolaadikook":
        hind = math.pi * m**2 * 0.06
    elif n == "ploomikook":
        hind = math.pi * m**2 * 0.04
    elif n == "Napoleoni kook":
        hind = m**2 * 0.10
    return round(hind, 2)

nimi = "a"

while nimi != "":
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõt: "))
   
    try:
        print(koogi_hind(nimi, mõõt))
    except:
        print("Sellist kooki andmebaasist ei leitud")