from math import pi
def koogi_hind(nimi, mõõt):
    if nimi=="šokolaadikook":
        return round(mõõt**2*pi*0.06,2)
    elif nimi=="ploomikook":
        return round(mõõt**2*pi*0.04,2)
    elif nimi=="Napoleoni kook":
        return round(mõõt**2*0.10,2)
    else:
        return error
while True:
    try:
        nimi=input("sisesta koogi nimi: ")
        if nimi=='':
            break
        mõõt=float(input("sisesta koogi mõõt sentimeetrites: "))
        print("kook maksab",koogi_hind(nimi,mõõt),"eurot")
    except:
      print("Sellist kooki andmebaasist ei leitud")



