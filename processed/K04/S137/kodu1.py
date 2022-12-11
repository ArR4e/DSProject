import math
def koogi_hind(nimi, mõõt):
    nimi = nimi.lower()
    mõõt = float(mõõt)
    if nimi == "šokolaadikook":
        mõõt = round(mõõt**2*math.pi*0.06,2)
        return mõõt
    elif nimi == "ploomikook":
        mõõt = round(mõõt**2*math.pi*0.04,2)
        return mõõt
    elif nimi == "napoleoni kook":
        mõõt = round(mõõt**2*math.pi*0.1,2)
        return mõõt
    else:
        return 0
kook = input("Sisesta koogi nimi :")
nr = input("Sisesta koogi mõõt:")
if koogi_hind(kook,nr) == 0:
    print("Sellist kooki andmebaasist ei leitud")
else:
    print("koogi hind tuleb", koogi_hind(kook,nr))


        
