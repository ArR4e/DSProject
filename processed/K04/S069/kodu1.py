from math import*
nimi = input("Kas sokolaadikook, ploomikook või Napoleoni kook? ")
mõõt = float(input("Koogi mõõt? "))

def koogi_hind(nimi, mõõt):
    if(nimi == 'sokolaadikook'):
        hind = 0.06*pi*(mõõt**2)
        hind = round(hind, 2)
        print(hind)
    elif(nimi == 'ploomikook'):
        hind = 0.04*pi*(mõõt**2)
        hind = round(hind, 2)
        print(hind)
    elif(nimi == 'Napoleoni kook'):
        hind = 0.10*mõõt*mõõt
        hind = round(hind, 2)
        print(hind)
    else:
        print("Sellist kooki andmebaasist ei leitud")

koogi_hind(nimi, mõõt)
        

    