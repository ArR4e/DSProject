koogi_nimi = input("Sisesta koogi nimi: ")
koogi_mõõt = float(input("Sisesta koogi mõõt: "))

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        S = 3.14 * (koogi_mõõt ** 2)
        hind_cm2_kohta = float(0.06)
    elif koogi_nimi == "ploomikook":
        S = 3.14 * (koogi_mõõt ** 2)
        hind_cm2_kohta = float(0.04)
    elif koogi_nimi == "Napoleoni kook":
        S = koogi_mõõt**2
        hind_cm2_kohta = float(0.1)
    else:
        print("Sellist kooki andmebaasist ei leitud")
    hind = S * hind_cm2_kohta
    return hind
hind = round(koogi_hind(koogi_nimi, koogi_mõõt), 2)
print("Koogi maksumus on " + str(hind))



         