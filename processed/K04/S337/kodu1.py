from math import pi
def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = mõõt**2*pi*0.06
    elif nimi == "ploomikook":
        hind = mõõt**2*pi*0.04
    elif nimi == "Napoleoni kook":
        hind = mõõt*mõõt*0.10
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return round(hind, 2)
while True:
    nimi = str(input("Sisestage koogi nimi: "))
    if nimi == "":
        break
    mõõt = float(input("Sisestage koogi mõõt sentimeetrites: "))
    print(koogi_hind(nimi, mõõt))
