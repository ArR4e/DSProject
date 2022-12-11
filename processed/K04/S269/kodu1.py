import math

def koogi_hind(n, d):
    if n == "šokolaadikook":
        return round((d)**2 * math.pi * 0.06,2)
    elif n == "ploomikook":
        return round((d)**2 * math.pi * 0.04,2)
    elif n == "Napoleoni kook":
        return round(d**2 * 0.1,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    nimi = input("Koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Koogi mõõt (cm): "))
    print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot.")

    
