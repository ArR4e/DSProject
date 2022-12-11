from math import pi

while True:
    
    nimi = input("Millist kooki tahad? (Šokolaadikook, ploomikook või Napoleoni kook) ")

    if nimi == "":
        break

    mõõt = float(input("Kui suurt kooki tahad? (cm) "))

    def koogi_hind(nimi, mõõt):
        if nimi == "šokolaadikook":
            return round(0.06 * mõõt * mõõt * pi, 2)
        elif nimi == "ploomikook":
            return round(0.04 * mõõt * mõõt * pi, 2)
        elif nimi == "Napoleoni kook":
            return round(0.10 * mõõt * mõõt, 2)
        else:
            raise ValueError("Sellist kooki andmebaasist ei leidu")


    print("Selle koogi hind on", koogi_hind(nimi, mõõt))
    
    
    




        
    
    