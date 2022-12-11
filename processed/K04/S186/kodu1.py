from math import pi
def koogi_hind(nimi, mõõt):
    while True:
        if nimi==šokolaadikook:
            pindala=pi*mõõt**2
            hind=0.06
            return (pindala*hind)
        elif nimi==ploomikook:
            pindala=pi*mõõt**2
            hind=0.04
            return (pindala*hind)
        elif nimi==napoleoni_kook:
            pindala=mõõt**2
            hind=0.10
            return (pindala*hind)
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud.")
        if nimi=="":
            break
    return round(hind*pindala, 2)

    print("Koogi hind on ",koogi_hind(nimi, mõõt)," eurot.")
koogi_hind=input("Sisesta koogi nimi ja mõõt: ")

