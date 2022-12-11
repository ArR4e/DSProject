from math import pi
def koogi_hind(nimi, mõõt):
    if nimi=="šokolaadikook":
        pindala=mõõt*mõõt*pi
        hind=0.06
        return round(hind*pindala, 2)
    elif nimi=="ploomikook":
        pindala= mõõt*mõõt*pi
        hind=0.04
        return round(hind*pindala, 2)
    elif nimi=="Napoleoni kook":
        pindala=mõõt*mõõt
        hind=0.1
        return round(hind*pindala, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud.")
while True:
    nimi=input("Sisesta koogi nimi: ")
    mõõt=float(input("Sisesta koogitüki mõõt: "))
    print("Koogitüki hind on", koogi_hind(nimi, mõõt), "eurot.")
    if nimi == "":
       break