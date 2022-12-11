from math import pi

def koogi_hind(nimi, suurus):


        if a == "šokolaadikook":
            pindala = suurus **2 * pi
            hind = pindala * 0.06

        if a == "Napoleoni kook":
            pindala = suurus**2
            hind = pindala * 0.10

        if a == "ploomikook":
            pindala = suurus **2 * pi
            hind = pindala * 0.04

        if nimi != "šokolaadikook" and nimi != "Napoleoni kook" and nimi != "ploomikook":
            raise Exception("Sellist kooki andmebaasist ei leitud")

        return round(hind, 2)

a = input("Sisestage soovitud kook: ")
b = float(input("Sisestage soovitud koogi mõõtmed cm: "))

print("Koogi hind on " + str(koogi_hind(a, b)) + " €.")

