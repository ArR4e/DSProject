from math import pi

def koogi_hind(nimi, moot):
    if nimi.strip().lower() == "šokolaadikook":
        return round((moot**2)*pi*0.06, 2)
    if nimi.strip().lower() == "ploomikook":
        return round((moot**2)*pi*0.04, 2)
    if nimi.strip().lower() == "napoleoni kook":
        return round((moot**2)*0.1, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
while True:
    nimi = str(input("Sisestage koogi nimi: "))
    if nimi == "":
        break
    moot = float(input("Sisetage koogi mõõt: "))
    
    print("Koogi hind on", koogi_hind(nimi, moot), "eurot")