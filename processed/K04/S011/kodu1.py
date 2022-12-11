from math import pi

def koogi_hind(nimi,mõõt) :
    if nimi != str(šokolaadikook) or nimi != str(ploomikook) or nimi != str(Napoleoni_kook) :
        raise Exception("Sellist kooki andmebaasist ei leitud")
    elif nimi == šokolaadikook :
        šokolaadikook = float(0.06)
        return round((nimi*(mõõt**2)*3.14),2)
    elif nimi == ploomikook :
        ploomikook = float(0.04)
        return round((nimi*(mõõt**2)*3.14),2)
    elif nimi == Napoleoni_kook :
        Napoleoni_kook = float(0.10)
        return round(mõõt**2,2)
    
while True:
    nimi = input("Millist kooki soovite osta? ")
    if nimi == "":
        break
    else:
        mõõt = float(input("Koogi mõõt (kas raadius või külje pikkus): "))
        print("Koogi hind on ", koogi_hind(nimi,mõõt), "€")