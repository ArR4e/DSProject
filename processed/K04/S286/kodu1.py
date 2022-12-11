from math import *
nimi = str(input("Millist kooki soovid?:"))
suurus = float(input("Sisestage koogi suurus:"))

def koogi_hind(nimi, suurus):
    if nimi != "šokolaadikook" and nimi != "ploomikook" and nimi!= "Napoleoni kook":
        print("Sellist kooki andmebaasist ei leitud")
    elif nimi == "šokolaadikook":
            hind1 = (pi*(suurus/2)**2)*0.06
            print("Koogitüki maksumus on " + str(round(hind1, 2)) + " eurot.")
            return hind1
    elif nimi == "ploomikook":
            hind2 = (pi*(suurus/2)**2)*0.04
            print("Koogitüki maksumus on " + str(round(hind2, 2)) + " eurot.")
            return hind2
    else:
        hind3 = (suurus**2)*0.1
        print("Koogitüki maksumus on " + str(round(hind3, 2)) + " eurot.")
        return hind3

koogi_hind(nimi, suurus)

while True:
    nimi = str(input("Millist kooki soovid?:"))
    if nimi != "šokolaadikook" and nimi != "ploomikook" and nimi!= "Napoleoni kook":
        break
    else:
        suurus = float(input("Sisestage koogi suurus:"))
        print("Koogi hind on: " +str(round(koogi_hind(nimi, suurus)))+ "eurot.")

