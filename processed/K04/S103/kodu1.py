import math

def koogi_hind(nimi, mõõt):
    pindala1 = float(math.pi*mõõt**2)
    pindala2 = float(mõõt*mõõt)
    if nimi == "šokolaadikook":
        return round(0.06 * pindala1, 2)
    elif nimi == "ploomikook":
        return round(0.04 * pindala1, 2)
    elif nimi == "Napoleoni kook":
        return round(0.10 * pindala2, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    

while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    if koogi_nimi == "":
        break
    mõõdud = float(input("Sisesta koogi mõõdud: "))
    print(koogi_hind(koogi_nimi,mõõdud))

