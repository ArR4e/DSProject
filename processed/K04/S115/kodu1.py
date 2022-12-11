from math import pi

def koogi_hind(nimi, mõõt):
        if nimi == "šokolaadikook":
            return round(0.06*(pi*mõõt**2),2)
        elif nimi == "ploomikook":
            return round(0.04*(pi*mõõt**2),2)
        elif nimi == "Napoleoni kook":
            return round(0.10*mõõt**2,2)
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõdu: "))
    print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot.")