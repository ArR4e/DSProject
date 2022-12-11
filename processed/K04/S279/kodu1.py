from math import pi

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        koogi_maksumus = (pi*koogi_mõõt**2)*0.06
        return round(koogi_maksumus, 2)
    elif koogi_nimi == "ploomikook":
        koogi_maksumus = (pi*koogi_mõõt**2)*0.04
        return round(koogi_maksumus, 2)
    elif koogi_nimi == "Napoleoni kook":
        koogi_maksumus = (koogi_mõõt**2)*0.10
        return round(koogi_maksumus, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
        
while True:
    koogi_nimi = input("Kirjuta koogi nimi: ")
    if koogi_nimi == "":
        break
    koogi_mõõt = float(input("Sisesta koogi mõõt sentimeetrites: "))
    print("Koogi maksumus eurodes on", koogi_hind(koogi_nimi, koogi_mõõt))
