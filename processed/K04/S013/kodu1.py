from math import pi


def koogi_hind(nimi, mõõt):
    
    if nimi == "šokolaadikook":
        hind = 0.06
        pindala = pi * float(mõõt)**2
        return round(hind*pindala, 2)
    elif nimi == "ploomikook":
        hind = 0.04
        pindala = pi * float(mõõt)**2
        return round(hind*pindala, 2)
    elif nimi == "Napoleoni kook":
        hind = 0.10
        pindala = (float(mõõt)**2)
        return round(hind*pindala, 2)
    else:
        print("Sellist kooki andmebaasist ei leitud")
x = True
while x:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    else:
        mõõt = input("Sisesta koogi mõõt: ")
        print("Koogi hind on ", koogi_hind(nimi, mõõt), "eurot.")
    
    


           
     
    