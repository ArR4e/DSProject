from math import pi

def koogi_hind(a,b):
    if a=="šokolaadikook":
        return round(pi*b**2*0.06,2)
    elif a=="ploomikook":
        return round(pi*b**2*0.04,2)
    elif a=="Napoleoni kook":
        return round(b**2*0.10,2)
    else:
        raise ValueError("Sellist kooki andmebaasis ei leitud.") #valueerrori jaoks https://progtugi.cs.ut.ee/#/ts/613e4881e857bcd80b002135/613f04b7e857bcd80b002301

nimi=input("Sisesta koogi nimi: ")
while nimi!="":
    mõõt=float(input("Sisesta koogi mõõt sentimeetrites: "))
    
    print("Koogi hind on",str(koogi_hind(nimi,mõõt)),"eurot.","\n")
    
    nimi=input("Sisesta koogi nimi: ")


    



