# Import math Libary
import math


def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi== ("Napoleoni kook"):
       hind = round(0.10*mõõt*mõõt,2)
       return hind
    if koogi_nimi==("šokolaadikook"):
        hind = round(0.06*mõõt**2*(math.pi),2)
        return hind
    if koogi_nimi ==("ploomikook"):
        hind=round(0.04*mõõt**2*(math.pi),2)
        return hind
    return Exception("Sellist kooki andmebaasist ei leitud.")
    
while True:
    nimi=str(input('Sisestage kooginimi: '))
    if nimi == (""):
        break
    mõõt=float(input("Sisestage koogi mõõt: "))
    print(koogi_hind(nimi, mõõt))
    

