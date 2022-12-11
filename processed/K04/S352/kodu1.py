from math import pi
def koogi_hind(kook,r):
    if kook=="šokolaadikook":
        return round(pi*r**2*0.06,2)
    elif kook=="ploomikook":
        return round(pi*r**2*0.04,2)
    elif kook=="Napoleoni kook":
        return round(r**2*0.10,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    try:
        kook=str(input("Sisestage koogi nimi "))
        if kook=="":
            break
        r=float(input("Sisestage koogi mõõt(cm) "))
        koogi_hind(kook,r)
        print(round(koogi_hind(kook,r),2),"€")
    except:
        print("Sellist kooki andmebaasist ei leitud")