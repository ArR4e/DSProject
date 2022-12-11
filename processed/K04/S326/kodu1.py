from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return(round((pi*mõõt**2)*0.06, 2))
    elif nimi == "ploomkook":
        return(round((pi*mõõt**2)*0.04, 2))
    elif nimi == "Napoleoni kook":
        return(round(mõõt**2, 2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    nimi = input("Koogi nimi: ")
    if nimi == "":
        break
    else:
        mõõt = float(input("Koogi mõõt: "))
        print("Koogi hind on ", koogi_hind(nimi, mõõt))
        
    