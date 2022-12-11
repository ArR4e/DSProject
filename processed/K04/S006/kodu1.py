from math import*

while True:
    nimi = input("Valikus on šokolaadikook, ploomikook ja Napoleoni kook. Milline kook on meelepäraseim? ")
    if nimi == "":
        break
    
    mõõt = float(input("Sisesta koogitüki suurus sentimeetrites: "))
    
    def koogi_hind(nimi, mõõt):
        if nimi == "šokolaadikook":
            return(round(mõõt*mõõt*0.06*pi, 2))
        elif nimi == "ploomikook":
            return(round(mõõt*mõõt*0.04*pi, 2))
        elif nimi == "Napoleoni kook":
            return(round(mõõt*mõõt*0.10, 2))
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud.")
    
    print("Koogitüki hind on ", koogi_hind(nimi, mõõt), " eurot.")



