from math import pi

def koogi_hind(nimi,mõõt):
    if nimi == "sokolaadikook" :
        return round(0.06*mõõt**2*pi,2)
    if nimi == "ploomikook" :
        return round(0.04*mõõt**2*pi,2)
    if nimi == "napoleoni kook" :
        return round(0.10*mõõt**2*pi,2)
    else:
        print("Sellist kooki ei leitud! ")
        
While True:
    nimi = input("Koogi nimi: ")
    if nimi == "":
        break
    mõõt = input("Suurus: ")
    print(koogi_hind(nimi, int(mõõt)))