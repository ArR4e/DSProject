from math import*

def koogi_hind(a, b):
    if a == "šokolaadikook":
        return(round(((pi*b**2)*0.06), 2))
    elif a == "ploomikook":
        return(round(((pi*b**2)*0.04), 2))
    elif a == "Napoleoni kook":
        return(round(((b**2)*0.1), 2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    nimi = str(input("Sisesta koogi nimi:"))
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõt:"))
    print(koogi_hind(nimi, mõõt))