from math import pi
def koogi_hind(koogi_nimi , moot):
    while True:
        if koogi_nimi == "šokolaadikook":
            koogi_nimi = 0.06
            return koogi_nimi * moot**2 * pi
        elif koogi_nimi == "ploomikook":
            koogi_nimi = 0.04
            return koogi_nimi * moot**2 * pi
        elif koogi_nimi == "Napoleoni kook":
            koogi_nimi = 0.1
            return koogi_nimi* moot**2
        elif koogi_nimi == "":
            break        
        else:
            print("Sellist kooki andmebaasist ei leitud")
            koogi_nimi = input("Sisesta koogi nimi: ")

koogi_nimi = input("Sisesta koogi nimi: ")
moot = float(input("Sisesta koogi mõõt: "))
try:
    kook = koogi_hind(koogi_nimi, moot)
    print(round(kook, 2))
except:
    none