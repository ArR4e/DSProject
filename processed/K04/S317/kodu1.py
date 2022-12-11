from math import pi
nimi = input("Sisesta kooginimi (šokolaadikook, ploomikook, Napoleoni kook): ")
mõõt1 = input("Sisesta raadius šokolaadikoogi ja ploomikoogi puhul, Napoleoni koogi puhul küljepikkus: ")
mõõt = float(mõõt1)
def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook" and mõõt > 0:
        pindala = pi * mõõt**2
        hind = round((pindala * 0.06), 2)
        print("Koogi hind on", hind, "EUR")
    else:
        if nimi == "ploomikook":
            pindala = pi * mõõt**2
            hind = round((pindala * 0.04), 2)
            print("Koogi hind on", hind, "EUR")
        else:
            if nimi == "napoleoni_kook":
                pindala = mõõt**2
                hind = round((pindala * 0.10), 2)
            else:
                print("Sellist kooki andmebaasist ei leitud")
koogi_hind(nimi, mõõt)