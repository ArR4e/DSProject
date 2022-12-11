from math import pi
from time import sleep

def ringi_pindala(raadius):
    return pi * raadius ** 2

def ruudu_pindala(pikkus):
    return pikkus ** 2


def koogi_hind(kook, moot):
    koogid = {"šokolaadikook": (0.06, "r"),
              "ploomikook": (0.04, "r") ,
              "napoleoni kook": (0.10, "k")}
    
    if kook not in koogid:
        raise Exception("Sellist kooki andmebaasist ei leitud!")
    
    if koogid[kook][1] == "r":
        hind = ringi_pindala(moot) * koogid[kook][0]
        return round(hind, 2)
    elif koogid[kook][1] == "k":
        hind = ruudu_pindala(moot) * koogid[kook][0]
        return round(hind, 2)
    
while True:
    print("""\n\n\n\n\n----------------------------------------------
Koogid: šokolaadikook  (ringikujuline)
        ploomikook     (ringikujuline)
        napoleonikook  (ruudukujuline)
----------------------------------------------""")
    sisend = input("Sisesta koogi nimi(Väljumiseks ENTER): ")
    if sisend == "":
        break
    x = float(input("Sisesta koogi mõõtmed (raadius, küljepikkus): "))
    hind = koogi_hind(sisend.lower(), x)
    print(f"\nSelle koogi hind on {hind}€")
    sleep(3)
    
    
    
    
    
    
    
    
    
    
    
    