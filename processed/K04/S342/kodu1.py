from math import pi
def koogi_hind(nimi, mõõt):
    hind = 0
    while nimi != "":
        nimi = nimi.strip('"')
        if nimi == "Napoleoni kook" or nimi == "šokolaadikook" or nimi == "ploomikook":
            if nimi == "Napoleoni kook":
                hind = round((mõõt ** 2 * 0.10), 2)
            elif nimi == "šokolaadikook":
                hind = round((mõõt**2 * pi * 0.06), 2) 
            elif nimi == "ploomikook":
                hind = round((mõõt**2 * pi * 0.04), 2)
            print(hind)
            nimi = input("Sisestage koogi nimi: ")
            if nimi == "":
                break
            mõõt = float(input("Sisestage koogi mõõt: "))
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud")

koogi_hind(input("Sisestage koogi nimi: "), float(input("Sisestage koogi mõõt: ")))