from math import pi
S_šokolaadikook = pi * mõõt**2
hind_šokolaadikook = 0,06*S_šokolaadikook
S_ploomikook = pi * mõõt**2
hind_ploomikook = 0,04*S_ploomikook
S_napoleonikook = mõõt**2
hind_napoleonikook = 0,10*S_napoleonikook

def koogi_nimi(nimi, mõõt):
    return  

while True:
    koogi_nimi = input("Koogi nimi: ")
    if (nimi == šokolaadikook):
        return koogi_mõõt
    elif (nimi == ploomikook):
        return koogi_mõõt
    elif (nimi == napoleonikook):
        return koogi_mõõt
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud.")
    if koogi_nimi == "":
        break
    koogi_mõõt = float(input("Koogi mõõt: "))
    koogi_hind = f
    print
    
    
print("Koogi hind on", koogi_hind(koogi_nimi, koogi_mõõt), "eurot.")