from math import pi

while True:
    def koogi_hind(koogi_nimi, koogi_mõõt):
        if koogi_nimi == "šokolaadikook":
            return round(0.06 * (pi * float(koogi_mõõt)**2), 2)
        elif koogi_nimi == "ploomikook":
            return round(0.04 * (pi * float(koogi_mõõt)**2), 2)
        elif koogi_nimi == "Napoleoni kook":
            return round(0.10 * (float(koogi_mõõt)**2), 2)
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud")

    koogi_nimi = input("Sisesta koogi nimi: ")
    if koogi_nimi == "":
            break
    
    koogi_mõõt = input("Sisesta koogi mõõt: ")
    
    print("Koogi hind on", koogi_hind(koogi_nimi, koogi_mõõt), "eurot.")