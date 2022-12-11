from math import*

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        koogi_hind = round((pi*mõõt**2)*0.06, 2)
        return koogi_hind
    
    elif nimi == "ploomikook":
        koogi_hind = round((pi*mõõt**2)*0.04, 2)
        return koogi_hind
    
    elif nimi == "Napoleoni kook":
        koogi_hind = round((mõõt**2)*0.10, 2)
        return koogi_hind
    
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

koogi_nimi = str(input("Sisestage koogi nimi: "))
koogi_mõõt = float(input("Sisestage koogi mõõt: "))
maksumus = koogi_hind(koogi_nimi, koogi_mõõt)

print("Koogi hind on", maksumus, "eurot.")