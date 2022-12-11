from math import pi

def koogi_hind(kooginimi, mõõt):   
    if kooginimi == "Napoleoni kook":
        return round(mõõt * mõõt * 0.10, 2)
    if kooginimi == "šokolaadikook":
        return round(0.06 * mõõt**2 * pi, 2)
    if kooginimi == "ploomikook":
        return round(0.04 * mõõt**2 * pi, 2)
        print("koogi hind on:", round(koogi_hind(kooginimi, mõõt), 2))
    else: 
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    kooginimi = str(input("Sisestage palun koogi nimi: "))
    if kooginimi == '':
        break
    mõõt = float(input("Sisestage koogi mõõt: "))
    print("koogi hind on:", round(koogi_hind(kooginimi, mõõt), 2))
