from math import pi


def koogi_hind(nimi, mõõt):
    
    if nimi == "šokolaadikook":
        pindala = mõõt*mõõt*pi
        hind = round(pindala * 0.06, 2)
        return hind
        
    if nimi == "ploomikook":
        pindala = mõõt*mõõt*pi
        hind = round(pindala * 0.04, 2)
        return hind
            
    if nimi == "Napoleoni kook":
        pindala = mõõt*mõõt
        hind = round(pindala * 0.1, 2)
        return hind
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
        
while True:  
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõt: "))
    print(koogi_hind(nimi, mõõt), "eurot.")
    
    


