from math import pi
def koogi_hind(koogi_nimi, koogi_mõõt):
    if (koogi_nimi=="šokolaadikook"):
        return round(((pi*koogi_mõõt**2)*0.06), 2)
    if (koogi_nimi=="ploomikook"):
        return round(((pi*koogi_mõõt**2)*0.04), 2)
    if (koogi_nimi=="Napoleoni kook"):
        return round(((koogi_mõõt**2)*0.10), 2)
    elif koogi_nimi!="":
        raise Exception("Sellist kooki andmebaasis ei ole.")
koogi_nimi=str(input("sisesta koogi nimi: "))
if koogi_nimi=="":
    exit()
koogi_mõõt=float(input("sisesta koogi mõõt:"))
while True:
    if (koogi_nimi=="šokolaadikook"):
        print(koogi_hind(koogi_nimi, koogi_mõõt))
        koogi_nimi=str(input("sisesta koogi nimi: "))
        if (koogi_nimi==""):
            break
        koogi_mõõt=float(input("sisesta koogi mõõt:"))
        continue
    if (koogi_nimi=="ploomikook"):
        print(koogi_hind(koogi_nimi, koogi_mõõt))
        koogi_nimi=str(input("sisesta koogi nimi: "))
        if (koogi_nimi==""):
            break
        koogi_mõõt=float(input("sisesta koogi mõõt:"))
        continue
    if (koogi_nimi=="Napoleoni kook"):
        print(koogi_hind(koogi_nimi, koogi_mõõt))
        koogi_nimi=str(input("sisesta koogi nimi: "))
        if (koogi_nimi==""):
            break
        koogi_mõõt=float(input("sisesta koogi mõõt:"))
        continue
    else:
        print("Sellist kooki andmebaasis ei ole.")
        koogi_nimi=str(input("sisesta koogi nimi: "))
        koogi_mõõt=float(input("sisesta koogi mõõt:"))
