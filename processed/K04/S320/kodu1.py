from math import pi


def koogi_hind(nimi, mõõt):
    
    ploomikook=round(pi*mõõt**2*0.04, 2)
    šokolaadikook=round(pi*mõõt**2*0.06, 2)
    Napoleoni_kook=round(mõõt**2*0.10, 2)


    if nimi=="ploomikook":
        return(ploomikook)
    elif nimi=="šokolaadikook":
        return(šokolaadikook)
    elif nimi=="Napoleoni kook":
        return(Napoleoni_kook)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    nimi=input("Sisesta koogi nimi:")
    if nimi=="":
        break
    mõõt=float(input("Sisesta koogi mõõt:")) 

  
    print(koogi_hind(nimi, mõõt))   


