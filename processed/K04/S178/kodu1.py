from math import pi

def koogi_hind(a,b):
    if a == "šokolaadikook":
        hind = (pi * b ** 2) * 0.06
        koos = round(hind, 2)
        print("Koogi hind on: ", koos , "eurot.")
    elif a == "ploomikook":
        hind = (pi * b ** 2) * 0.04
        koos = round(hind, 2)
        print("Koogi hind on: ", koos , "eurot.")
    elif a == "Napoleoni kook":
        hind = (b * b) * 0.1
        koos = round(hind, 2)
        print("Koogi hind on: ", koos , "eurot.")

    else:
        print("Sellist kooki andmebaasist ei leitud")
    
while True:
    a = input("Sisesta koogi nimi, kas šokolaadikook, ploomikook või Napoleoni kook: ")
    if a == "":
        break
    b = float(input("Sisesta koogi mõõt sentimeetrites: "))


    koogi_hind(a,b)
