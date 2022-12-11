from math import pi
kook=(input('Sisestage koogi nimi: '))
i=0
while True:
    moot=float(input('Sisestage läbimõõt: '))
    def koogi_hind(kook, moot):
        if kook == "šokolaadikook":
            hind=0.06*(pi*(moot**2))
        elif kook == "ploomikook":
            hind=0.04*(pi*(moot**2))
        elif kook== "Napoleoni kook":
            hind=0.10*(moot**2)
        else:
            print('Sellist kooki andmebaasist ei leitud')
        hind=round(hind,2)
        print(str(hind) + '€')
    kook=(input('Sisestage koogi nimi: '))
    if kook =="":
        break