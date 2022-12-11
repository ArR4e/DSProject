from math import pi
def koogi_hind(koogi_nimi, mõõt):
    ruut = mõõt**2
    try:
        if koogi_nimi == "ploomikook":
            hind = round(0.04*ruut*pi, 2)
        elif koogi_nimi == "šokolaadikook":
            hind = round(0.06*ruut*pi, 2)
        elif koogi_nimi == "Napoleoni kook":
            hind = round(0.1*ruut, 2)
        print("Koogi hind on", hind, "eurot.")        
    except:
        print("Sellist kooki andmebaasist ei leitud")
while True:
    koogi_nimi = input("Mis kooki soovid? ")
    if koogi_nimi == "":
        break
    mõõt = float(input("Kui suurt kooki soovid (sentimeetrites + üks koht pärast koma): "))
    koogi_hind(koogi_nimi, mõõt)
