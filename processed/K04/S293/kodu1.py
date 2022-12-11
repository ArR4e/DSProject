from math import pi
def koogi_hind(nimi, moot):

    if nimi=="šokolaadikook":
        return(round(moot**2 * pi * 0.06, 2))
    elif nimi=="ploomikook":
        return(round(moot**2 * pi * 0.04, 2))
    elif nimi=="Napoleoni kook":
        return(round(moot**2 * 0.1, 2))
    else:
        raise Exception("Sellist kooki andmebaasis pole")

i=0

while i<1:
    nimi=input("Sisestage koogi nimi: ")             
    if nimi!="":
        moot=float(input("Sisestage koogi mõõt: "))
        print("Koogi hind on", koogi_hind(nimi, moot), "eurot")
        
    else:
        break    