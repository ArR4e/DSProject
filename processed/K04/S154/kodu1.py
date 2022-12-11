from math import *

nimi = str(input("Sisestage koogi nimi: "))
suurus = float(input("Sisestage koogi mõõt: "))

i = 0
soko = 0.06
ploom = 0.04
napo = 0.10
hind = 0

def koogi_hind(nimi, suurus):
    if nimi == soko or ploom:
        return (suurus**2 * pi) * float(nimi)
    elif kook == napo:
        return (suurus**2) * nimi
    else:
        print("Sellist kooki andmebaasist ei leitud.")
    
while i < 1 and nimi != "":
    print(koogi_hind(nimi, suurus))