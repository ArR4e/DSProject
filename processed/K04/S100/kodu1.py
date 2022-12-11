from math import pi

def koogi_hind(nimi, suurus):
    if nimi == "šokolaadikook":
        hind = 0.06*pi*suurus**2
    elif nimi == "ploomikook":
        hind = 0.04*pi*suurus**2
    elif nimi == "Napoleoni kook":
        hind = 0.1*suurus**2
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    return round(hind, 2)

while True:
    kooginimi = input("Sisestage koogi nimi: ")
    if len(kooginimi) == 0:
        break
    moot = float(input("Sisestage koogi mõõt: "))
    print(koogi_hind(kooginimi, moot))