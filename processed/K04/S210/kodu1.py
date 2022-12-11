from math import pi 
def koogi_hind(nimi, moot):
    if nimi == "šokolaadikook":
        return (round((0.06 * pi * moot** 2),2 ))
    elif nimi == "ploomikook":
        return (round((0.04 * pi * moot** 2),2))
    elif nimi == "Napoleoni kook":
        return (round(0.1 * (moot*moot),2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")

while True:
    nimi = (input("Sisestage koogi nimi: "))
    if nimi == "":
        break
    moot = float(input("Sisestage koogi mõõt: "))
    print ((koogi_hind(nimi, moot)))
