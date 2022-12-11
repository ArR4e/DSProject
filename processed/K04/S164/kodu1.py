from math import pi 



def koogi_hind(kooginimi, mõõt):
    
    if kooginimi == "šokolaadikook":
        pindala = pi * mõõt ** 2
        hind = pindala * 0.06
        return round(hind, 2)
        
   
    elif kooginimi == "ploomikook":
        pindala = pi * mõõt ** 2
        hind = pindala * 0.04
        return round(hind, 2)
        
    elif kooginimi == "Napoleoni kook":
        pindala = mõõt ** 2
        hind = pindala * 0.1
        return round(hind, 2)
        
    else:
        return "Sellist kooki andmebaasist ei leitud"

while True: 
    
    kooginimi = input("Sisesta kooginimi: ")
    if kooginimi == "":
        break
    
    mõõt = int(input("Sisesta koogi mõõt: "))    
    hind = koogi_hind(kooginimi, mõõt)

    print (hind)
#šokolaadikook_mõõt = 0.06€/cm**2
#ploomikook_mõõt = 0.04€/cm**2
#napoleonikook_mõõt = 0.10€/cm**2
    
   