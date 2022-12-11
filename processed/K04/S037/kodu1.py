from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "Napoleoni kook":
        mõõt = mõõt ** 2
        return round((mõõt * 0.10),2)
    
    elif nimi == "šokolaadikook":
        mõõt = mõõt ** 2 * pi
        return round((mõõt * 0.06),2)
        
    elif nimi == "ploomikook":
        mõõt = mõõt ** 2 * pi
        return round((mõõt * 0.04),2)
        
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
  

while True:
    nimi = str(input("Sisestage koogi nimi: "))
    if nimi == "":
        break
    else:
        mõõt = float(input("Sisestage koogi mõõt: "))
        print("Koogi hind on " + str(koogi_hind(nimi, mõõt)) + " €.")
        continue
