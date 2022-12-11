from math import *
hind=0
while True:
    nimi = str(input("Milline on koogi nimi? "))
    if nimi=="":
        break
    moot = float(input("Sisestage koogi mõõdu(cm): "))
    def koogi_hind(x):
        if nimi == "šokolaadikook":
            return((pi*((x/2)**2))*0.06)
        elif nimi == "ploomikook":
             return((pi*((x/2)**2))*0.04)
        elif nimi == "Napoleoni kook":
            return(0.1*(x**2))
        else:
            print("Sellist kooki andmebaasist ei leitud")
            return 0
    print("Koogi hind on", round(koogi_hind(moot),2))
