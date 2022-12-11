from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return round(pi*mõõt**2*0.06,2)
    
    if nimi == "ploomikook":
        return round(pi*mõõt**2*0.04,2)
        
    if nimi == "Napoleoni kook":
        return round(mõõt**2*0.10,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")

nimi=input("Koogi nimi: ")

while nimi != "":
    mõõt=float(input("Mõõt: "))
    print("Koogi hind on " + str(koogi_hind(nimi, mõõt)) + " eurot.")
    nimi=input("Koogi nimi: ")
