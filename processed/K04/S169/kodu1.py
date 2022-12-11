import math as m
def koogi_hind(kooginimi, koogimõõt):
    if kooginimi == "šokolaadikook":
        pindala = koogimõõt**2 * m.pi
        return round(pindala*0.06,2)
    if kooginimi == "ploomikook":
        pindala = koogimõõt**2 * m.pi
        return round(pindala*0.04,2)
    if kooginimi == "Napoleoni kook":
        pindala = koogimõõt**2
        return round(pindala * 0.1,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    
    kooginimi = input("Sisesta koogi nimi: ")
    if kooginimi == "":
        break
    koogimõõt = float(input("Sisesta koogi raadius või küljepikkus: "))
    print(koogi_hind(kooginimi, koogimõõt))
    