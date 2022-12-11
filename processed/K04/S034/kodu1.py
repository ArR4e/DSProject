from math import pi

def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi != "Napoleoni kook" and koogi_nimi != "ploomikook" and koogi_nimi != "šokolaadikook":
        raise Exception ("Sellist kooki andmebaasist ei leitud.")
    elif koogi_nimi == "Napoleoni kook":
            pindala1 = mõõt**2
            N_koogi_hind = 0.10 # €/cm**2
            hind = round(N_koogi_hind * pindala1,2)
            return hind
    else:
        pindala2 = pi * mõõt**2
        if koogi_nimi == "ploomikook":
            p_koogi_hind = 0.04 # €/cm**2
            hind = round(pindala2 * p_koogi_hind,2)
            return hind
        else:
            š_koogi_hind = 0.06 # €/cm**2
            hind = round(pindala2 * š_koogi_hind,2)
            return hind


while True:
    koogi_nimi = input("Palun sisesta koogi nimi: ")
    if koogi_nimi == "":
        break
    mõõt = float(input("Palun sisesta koogi mõõt: "))
    print("Koogi hind on", koogi_hind(koogi_nimi, mõõt), "eurot.")