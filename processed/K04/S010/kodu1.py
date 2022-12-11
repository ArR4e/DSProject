from math import pi
while True:
    nimi=input("Sisestage soovitava koogi nimi: ")
    if nimi=="":
        break
    mõõt=float(input("Sisestage soovitava koogi raadius/küljepikkus: "))
    def koogi_hind(nimi, mõõt):
        if nimi !="šokolaadikook" and nimi!="ploomikook" and nimi!="Napoleoni kook":
            raise Exception("Sellist kooki andmebaasist ei leitud")
        if nimi=="šokolaadikook":
            hind=0.06*pi*mõõt**2
        if nimi=="ploomikook":
            hind=0.04*pi*mõõt**2
        if nimi=="Napoleoni kook":
            hind=0.1*mõõt**2
        return round(hind, 2)
    maksumus=koogi_hind(nimi, mõõt)
    print("Koogi hind on " + str(maksumus) + " eurot.")
    