from math import *

def koogi_hind(kook, moot):
    if kook == "šokolaadikook":
        a = moot**2 * pi * 0.06
        a = round(a, 2)
        return a
    elif kook == "ploomikook":
        a = moot**2 * pi * 0.04
        a = round(a, 2)
        return a
    elif kook == "Napoleoni kook":
        a = moot*moot* 0.10
        a = round(a, 2)
        return a
    elif kook != "šokolaadikook" or kook != "ploomikook" or kook != "Napoleoni kook":
        raise Exception("Sellist kooki andmebaasist ei leitud.")
while True:
    kook = input("Sisesta koogi nimi: ")
    if kook == "":
        break
    moot = float(input("Sisesta koogi mõõt: "))

    print(koogi_hind(kook,moot))
    
    
        

    

# print(koogi_hind("šokolaadikook" , 100))
# print(koogi_hind("ploomikook", 100))
# print(koogi_hind("Napoleoni kook", 100))
# print(koogi_hind("tere" , 100))
