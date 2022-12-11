import math

def koogi_hind(a,b):
    
    if a!="šokolaadikook" and a!="ploomikook" and a!="Napoleoni kook":
        raise Exception("Sellist kooki andmebaasist ei leitud")
    elif a=="šokolaadikook":
        return(round((math.pi*b**2)*0.06, 2))
    elif a=="ploomikook":
        return(round((math.pi*b**2)*0.04, 2))
    elif a=="Napoleoni kook":
        return(round((b**2)*0.1, 2))

while True:
    
    kook=str(input("Sisesta koogi nimi: "))
    if kook=="":
        break
    m66t=float(input("Sisesta mõõt: "))
    print(str(koogi_hind(kook,m66t)))
    
    


    

        
    