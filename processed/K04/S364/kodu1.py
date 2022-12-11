import math
def koogi_hind(kook, mõõt):
    if kook == "šokolaadikook":
        hind = 0.06
        pindala = mõõt**2*(math.pi)
        return round(hind*(pindala),2)
    elif kook == "ploomikook":
        hind = 0.04
        pindala = mõõt**2*(math.pi)
        return round(hind*(pindala),2)
    elif kook == "Napoleoni kook":
        hind = 0.10
        pindala = mõõt**2
        return round(hind*(pindala),2)
    else:
        raise Exception("Sellist koogi andmebaasist ei leitud")
while True:
    tortik = input("Sisestage koogi nimi: ")
    if tortik == "":
        break
    else:
        size = float(input("Sisestage koogi mõõdu: "))
        print(koogi_hind(tortik, size))
        continue

