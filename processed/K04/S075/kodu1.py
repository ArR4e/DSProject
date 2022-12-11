from math import *

def koogi_hind(kook,pikkus):
    if kook=="šokolaadikook":
        suurus=pi*float(pikkus)**2
        return round(suurus*0.06,2)
    elif kook=="ploomikook":
        suurus=pi*float(pikkus)**2
        return round(suurus*0.04,2)
    elif kook=="Napoleoni kook":
        suurus=float(raadius)**2
        return round(suurus*0.10,2)
    else:
        raise Exception()
        
kook=input("Sisesta koogi nimi: ")
pikkus=input("Sisesta koogi pikkus(cm): ")

while bool(kook=="")==False:
    try: 
        print(koogi_hind(kook,pikkus))
    except:
        print("Sellist kooki andmebaasist ei leitud")
    kook=input("Sisesta koogi nimi: ")
    pikkus=input("Sisesta koogi pikkus(cm): ")

