import math

def koogi_hind(nimi, mõõt):
    pindala = math.pi*(mõõt*mõõt)
    if nimi == "šokolaadikook":
        return(round(pindala*0.06, 2))
    elif nimi == "ploomikook":
        return(round(pindala*0.04, 2))
    elif nimi == "Napoleoni kook":
        return(round(pindala*0.1, 2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    nimi = input("Sisestage koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisestage koogi raadius (cm): "))
    print(koogi_hind(nimi, mõõt))