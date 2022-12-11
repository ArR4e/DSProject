from math import pi
koogi_nimi=str(input("koogi nimi"))
koogi_mõõt=float(input("koogi mõõt"))        

def koogi_hind(x, y):
    global koogihind
    if koogi_nimi == "šokolaadikook":
        koogihind = (pi*(koogi_mõõt)**2)*0.06
        print((str(round(koogihind, 2)) + "€"))
        return koogihind    
        
    elif koogi_nimi == "ploomikook":
        koogihind = pi*(koogi_mõõt)**2*0.04
        print((str(round(koogihind, 2)) + "€"))
        return koogihind
    elif koogi_nimi == "Napoleoni kook":
        koogihind = (koogi_mõõt)**2*0.1
        print((str(round(koogihind, 2)) + "€"))
        return koogihind
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while koogi_nimi == "šokolaadikook" or "ploomikook" or "Napoleoni kook" or "":
    if koogi_nimi == "šokolaadikook" or "ploomikook" or "Napoleoni kook":
        koogi_hind(koogi_nimi, koogi_mõõt)
        
        koogi_nimi=str(input("koogi nimi"))
        if koogi_nimi =="":
            break
        else:
            koogi_mõõt=float(input("koogi mõõt")) 
            continue

