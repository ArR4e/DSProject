from math import *

def koogi_hind(kn, mõõt):
    try:
        if kn == "šokolaadikook":
            return(round(((pi * (mõõt**2))*0.06), 2))
        elif kn == "ploomikook":
            return(round(((pi * (mõõt**2))*0.04), 2))
        elif kn == "Napoleoni kook":
            return(round(((mõõt**2)*0.10), 2))
        else:
            return(x)
    except:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    kn = input("Sisestage koogi nimi: ")
    
    if kn == "":
        break
    else:
        mõõt = float(input("Sisestage koogi mõõt (raadius või küljepikkus: "))
        print(koogi_hind(kn, mõõt))
        
        