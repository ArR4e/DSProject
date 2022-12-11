from math import pi 

def koogi_hind(nimi,mõõt):
    if nimi == "sokolaadikook" :
        return round(pi * 0.06 * mõõt ** 2,2)
    elif nimi == "ploomikook" :
        return round (pi * 0.04 * mõõt ** 2,2)
    elif nimi == "napoleoni kook" :
        return round (0.1 * mõõt ** 2,2)
    else:
        raise ValueError ("Sellist kooki andmebaasist ei leitud")
    
while True:
    nimi = str(input("Siia kirjutage palun koogi nimi: "))
    if nimi =="" :
        break
    mõõt = float(input("Siia kirjutage palun koogi suurus: "))
    print(koogi_hind(nimi,mõõt))
    


    


