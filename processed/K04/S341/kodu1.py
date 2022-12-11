from math import pi
n= input("Sisestage kooginimi:")
m= float(input("Sisestage koogimõõt:"))
def koogi_hind(nimi,mõõt):
    global n
    global m
    n= nimi
    m= mõõt
    if  nimi == "sokolaadikook" and mõõt == 0.06:
        return(round(pi**2/mõõt,2))
    elif nimi == "ploomikook" and mõõt == 0.04:
        return(round(pi**2/mõõt,2))
    elif nimi == "napoleonikook" and mõõt== 0.10:
        return(round(mõõt/mõõt**2, 2))
    else:
        raise ValueError("Pole sellist kooki andmebaasis.")

koogi_hind(n,m)
print("Koogi hind on ", koogi_hind(n,m), "eurot.")