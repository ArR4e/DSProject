
#küsime kogi nime ja mõõdu, kordame kuni jääb sisestamata ja enter
from math import pi 
def koogi_hind(a,b):
    while a==("šokolaadikook"):
        t=pi*b**2
        hind=t*0.06
        return round(hind,2)
    if a==("ploomikook"):
        t=pi*b**2
        hind=t*0.04
        return round(hind,2)
    if a==("Napoleoni kook"):
        t=b**2
        hind=t*0.10
        return round(hind,2)
    else:
        print("Sellist kooki meil pole")
        

a=input("Sisesta koogi nimi: ")

while a!=(""):
    if a!=("Napoleoni kook") and a!=("ploomikook") and a!=("šokolaadikook"):
        print("Sellist kooki meil pole")
        break
    else:
        b=float(input("Sisesta koogi mõõt: "))
        print("Koogi hind on: "+str(koogi_hind(a,b))+" eurot")
        a=input("Sisesta koogi nimi: ")
    
else:
    print("Programm lõppes")