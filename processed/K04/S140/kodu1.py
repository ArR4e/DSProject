from math import pi

def koogi_hind(kook, mõõt):
    if mõõt < 0:
        raise Exception("Koogi mõõt ei saa olla negatiivne")
    
    if kook == "šokolaadikook":
        return round(pi*mõõt**2 * 0.06, 2)
        
    elif kook == "ploomikook":
        return round(pi*mõõt**2 * 0.04, 2)
        
    elif kook == "Napoleoni kook":
        return round(mõõt**2 * 0.1, 2)
        
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    k = input("Sisestage koogi nimi: ")
    if k == "":
        break
    m = float(input("Sisestage koogi mõõt: "))
    print("Koogi hind on", str(koogi_hind(k, m)) + "€")
    