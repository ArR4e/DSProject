from math import pi

koogid = {
    "šokolaadikook": 0.06,
    "ploomikook": 0.04,
    "Napoleoni kook": 0.1
}

def koogi_hind(nimi, mõõt):
    if nimi not in list(koogid.keys()):
        raise Exception("Sellist kooki andmebaasist ei leitud")
    pindala = 0
    if nimi == "Napoleoni kook":
        pindala = mõõt * mõõt
    else:
        pindala = pi * mõõt * mõõt
    hind = pindala * koogid[nimi]
    return round(hind,2)

while True:
    nimi = input("nimi: ")
    
    if nimi == "":
        break
    
    mõõt = float(input("mõõt: "))
    print(koogi_hind(nimi, mõõt))

