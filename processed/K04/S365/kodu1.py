from math import*

    
def koogi_hind(koogi_nimi, mõõt):

    if koogi_nimi == "šokolaadikook":
        return(round((0.06*(pi*(mõõt**2))), 2))
    if koogi_nimi == "ploomikook":
        return(round((0.04*(pi*(mõõt**2))), 2))
    if koogi_nimi == "Napoleoni kook":
        return(round(0.10*(mõõt**2),2))
    raise Exception("Sellist kooki andmebaasist ei leitud")
        

while True:
    koogi_nimi = input("Mis on koogi sort? ")
    if koogi_nimi == "":
        break
    mõõt = float(input("mis on koogi mõõt? "))

    print(koogi_hind(koogi_nimi, mõõt))
    
    
    