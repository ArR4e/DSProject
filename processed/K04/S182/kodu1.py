from math import pi
def koogi_hind(kooginimi, mõõt):
    if (kooginimi== "šokolaadikook"):
        koogipindala=pi*float(mõõt)**2
        hind=koogipindala*0.06
        return round(hind, 2)
    elif (kooginimi== "ploomikook"):
        koogipindala=pi*float(mõõt)**2
        hind=koogipindala*0.04
        return round(hind, 2)
    elif (kooginimi== "Napoleoni kook"):
        koogipindala=float(mõõt)**2
        hind=koogipindala*0.10
        return round(hind, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud")
while True:
    try:
        kooginimi=input("Sisesta kooginimi: ")
        mõõt=input("Sisesta koogimõõt: ")

        if kooginimi=="":
            break
        else:
            print(koogi_hind(kooginimi, mõõt))
    except:
        print("Sellist kooki andmebaasist ei leitud")
