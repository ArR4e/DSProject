
from math import pi

def koogi_hind(koogi_nimi, koogi_moot):
    if koogi_nimi=="šokolaadikook":
        sokkoogi_pindala=pi * ((koogi_moot)**2)
        sokkoogi_hind=sokkoogi_pindala*0.06
        sokkoogi_hind=round(sokkoogi_hind, 2)
        return sokkoogi_hind
    elif koogi_nimi=="ploomikook":
        plokoogi_pindala=pi * ((koogi_moot)**2)
        plokoogi_hind=plokoogi_pindala*0.04
        plokoogi_hind=round(plokoogi_hind, 2)
        return plokoogi_hind
    elif koogi_nimi=="Napoleoni kook":
        napkoogi_pindala=koogi_moot**2
        napkoogi_hind=napkoogi_pindala*0.1
        napkoogi_hind=round(napkoogi_hind, 2)
        return napkoogi_pindala
    elif koogi_nimi!="šokolaadikook" and koogi_nimi!="ploomikook" and koogi_nimi!="Napoleoni kook":
        raise Exception("Sellist kooki andmebaasist ei leitud")
        #print("Sellist kooki andmebaasist ei leitud")

    
while True:        
    koogi_nimi=input("Sisestage koogi nimi: ")
    if koogi_nimi=="":
        break
    else:
        koogi_moot=float(input("Sisestage koogi raadius või külje pikkus sendimeetrites: "))
        print(koogi_hind(koogi_nimi, koogi_moot))
        
    
    