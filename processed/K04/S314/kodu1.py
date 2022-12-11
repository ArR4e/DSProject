from math import pi

def koogi_hind(kooginimi,koogimõõt):
    if kooginimi == "šokolaadikook":
        x = 0.06
        return round(x * pi * koogimõõt ** 2, 2)
    elif kooginimi == "ploomikook":
        x = 0.04
        return round(x * pi * koogimõõt ** 2, 2)
    elif kooginimi == "Napoleoni kook":
        x = 0.1
        return round(x * koogimõõt ** 2, 2)
        

while True:
    kooginimi = input("Sisesta koogi nimi: ")
    if kooginimi == "":
        break
    elif kooginimi == "šokolaadikook" or kooginimi == "ploomikook" or kooginimi == "Napoleoni kook":
        koogimõõt = float(input("Sisesta koogi mõõt: "))  
        print("Koogi hind on: ", koogi_hind(kooginimi,koogimõõt), "€")
    else: 
        print("Sellist kooki andmebaasist ei leitud")

