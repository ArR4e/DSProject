from math import pi
def koogi_hind(nimi,mõõt):
    if nimi == "napoleoni kook":
        hind = mõõt**2*0.1
    elif nimi == "šokolaadikook":
        hind = mõõt**2*pi*0.06
    elif nimi == "ploomikook":
        hind = mõõt**2*pi*0.04
    return round(hind,2)
while True:
    nimi = input("Millise koogi hinda soovite teada(šokolaadikook/ploomikook/napoleoni kook)? ")
    if nimi == "":
        break
    elif nimi == "šokolaadikook" or nimi == "ploomikook" or nimi == "napoleoni kook":
        mõõt = float(input("Mis on teie koogi raadius/külje pikkus? "))
        print("Teie koogi hind on", str(koogi_hind(nimi,mõõt))+"€")
    else:
        print("Sellist kooki andmebaasist ei leitud.")
