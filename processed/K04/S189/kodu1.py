import math

#šokolaadikook = mõõt**2 * math.pi * 0.06
#ploomikook = mõõt**2 * math.pi * 0.04
#napoleoni_kook = mõõt**2 * 0.10

koogid=["šokolaadikook","ploomikook","Napoleoni kook"]

def koogi_hind(kook, mõõt):
    if kook in koogid:
        if (kook=="šokolaadikook"):
            alghind= float(mõõt)**2 * math.pi * 0.06
            hind=round(alghind,2)
            print("Koogi hind on:",hind, "eurot")
            
        if (kook=="ploomikook"):
            alghind= float(mõõt)**2 * math.pi * 0.04
            hind=round(alghind,2)
            print("Koogi hind on:",hind, "eurot")
            
        if (kook=="Napoleoni kook"):
            alghind= float(mõõt)**2 * 0.10
            hind=round(alghind,2)
            print("Koogi hind on:",hind, "eurot")
    else:
        print("Sellist kooki andmebaasist ei leitud.")
    
while koogid:
    kook = str(input("Koogi nimi: "))
    if (kook==('')):
        exit()
    mõõt = input("Koogi mõõt: ")
    if (kook=="šokolaadikook"):
        koogi_hind(kook, mõõt)
        continue
    if (kook=="ploomikook"):
        koogi_hind(kook, mõõt)
        continue
    if (kook=="Napoleoni kook"):
        koogi_hind(kook, mõõt)
        continue
    else:
        print("Sellist kooki andmebaasist ei leitud.")
        continue


koogi_hind(kook,mõõt)

