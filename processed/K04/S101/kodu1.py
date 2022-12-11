from math import pi


def koogi_hind(koogi_nimi,koogi_mõõt):
    while  True:
        if koogi_nimi=="šokolaadikook":
            return (round(koogi_mõõt**2*pi*0.06,2))
        elif koogi_nimi=="ploomikook":
            return(round(koogi_mõõt**2*pi*0.04,2))
        elif koogi_nimi=="Napoleoni kook":
            return(round(koogi_mõõt**2*0.1,2))
        else:
            raise Exception("Sellist kooki pole andmebaasis")
        
while True:
    
    nimi=str(input("sisesta koogi nimi:"))
    if nimi=="":
        break
    mõõt=float(input("sisesta koogi mõõt:"))
    print("selle koogi hind on",koogi_hind(nimi,mõõt),"eurot")