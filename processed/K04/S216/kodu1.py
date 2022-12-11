from math import pi
def koogi_hind(hind,moot):
    if hind == "šokolaadikook":
        pindala = pi * moot**2
        oigehind = round(0.06*pindala,2)
        
        return oigehind
    elif hind == "ploomikook":
        pindala = pi * moot**2
        oigehind = round(0.04*pindala,2)
        
        return oigehind
    elif hind == "Napoleoni kook":
        pindala = moot**2
        oigehind = round(0.10*pindala,2)
        
        return oigehind
    else:
        print("Sellist kooki andmebaasist ei leitud")

while True:
    hind = str(input("Sisesta koogi tüüp: "))
    if hind == "":
        break
    moot = float(input("Sisesta koogi mõõt: "))
    print(koogi_hind(hind,moot))