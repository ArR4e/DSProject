from math import *
def koogi_hind(koogi_nimi,mõõt):
    
    if koogi_nimi=="šokolaadikook":
        pindala=pi * mõõt**2
        koogi_maksumus=round(0.06*pindala,2)
    elif koogi_nimi=="ploomikook":
        pindala=pi * mõõt**2
        koogi_maksumus=round(0.04*pindala,2)
    elif koogi_nimi=="Napoleoni kook":
        pindala= mõõt**2
        koogi_maksumus=round(0.1*pindala,2)
    elif koogi_nimi!="šokolaadikook" and koogi_nimi!="ploomikook" and koogi_nimi!="Napoleoni kook" :
        raise Exception("Sellist kooki andmebaasist ei leitud.")
           
    return koogi_maksumus 
    
           
    

while True:
    koogi_nimi=input("Sisestage koogi nimi: ")
    if koogi_nimi=="":
        break
    mõõt= float(input("Sisestage koogi mõõt: "))
    hind=koogi_hind(koogi_nimi, mõõt)
    
    print(str(hind)+ " eurot.")


#print(str(hind).strip("None"))

