from math import pi

def koogi_hind (koogi_nimi, koogi_moot):
    if (koogi_nimi == "Šokolaadikook"):
        return round((koogi_moot ** 2)* pi * 0.06, 2)
    elif (koogi_nimi == "Ploomikook"):
        return round((koogi_moot ** 2) * pi * 0.04, 2)
    elif (koogi_nimi == "Napoleoni kook"):
        return round((koogi_moot ** 2) * 0.10, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud.")


while True:
    koogi_nimi = input("Sisesta koogi nimi :")
    koogi_moot = float(input("Sisesta koogi mõõt: "))
    print("Koogi hind on ",koogi_hind(koogi_nimi, koogi_moot))
    if koogi_nimi == "":
        break
    

        
    
    
    
    