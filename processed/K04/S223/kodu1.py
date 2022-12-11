import math

def koogi_hind(nimi, raadius):
    if nimi == "šokolaadikook":
        return round(math.pi * raadius ** 2 * 0.06,2)
    elif nimi == "ploomikook":
        return round(math.pi * raadius ** 2 * 0.04,2)
    elif nimi == "Napoleoni kook":
        return round(raadius ** 2 * 0.1,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
        

while True:
    nimi = input("Sisestage koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisestage koogi mõõtmed: "))

    print(koogi_hind(nimi, mõõt))