import math

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi.lower() == "šokolaadikook":
        return round((koogi_mõõt**2 * math.pi) * 0.06 , 2)
    elif koogi_nimi.lower() == "ploomikook":
        return round((koogi_mõõt**2 * math.pi) * 0.04 , 2)
    elif koogi_nimi.lower() == "napoleoni kook":
        return round((koogi_mõõt ** 2) * 0.10, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
           
while True:
    a = str(input("Sisesta koogi nimi: "))
    if a == "":
        break
    b = float(input("Sisesta koogi pikkus: "))

    print(a, "koogi hind on: ", koogi_hind(a, b), "€" )    