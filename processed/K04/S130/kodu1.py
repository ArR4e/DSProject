from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == str('šokolaadikook'):
        return (round(mõõt**2*pi*0.06,2))
    elif nimi == str('ploomikook'):
        return (round(mõõt**2*pi*0.04,2))
    elif nimi == str('Napoleoni kook'):
        return (round(mõõt*mõõt*0.10,2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
    
while True:
    nimi = str(input("Sisestage koogi nimi: "))
    if nimi == (''):
        break
    mõõt = float(input("Sisestage koogi suurus: "))
    
    print("Koogi hind on",koogi_hind(nimi,mõõt), "eurot.")