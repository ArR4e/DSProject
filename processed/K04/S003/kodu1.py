from math import pi
def koogi_hind(kooginimi, moot):
    if kooginimi == "šokolaadikook":
        return round(pi * (moot **2 ) * 0.06, 2)
    elif kooginimi == "ploomikook":
        return round(pi * (moot **2 ) * 0.04, 2)
    elif kooginimi == "Napoleoni kook":
        return round(moot ** 2 * 0.10, 2)
    else:
        raise Exception("Sellist koooki andmebaasist ei leitud.")
    
while True:
    kooginimi = input("Palun sisesta koogi nimi: ")
    if kooginimi == "":
        break
    moot = float(input("Palun sisesta koogi mõõt: "))
    print(koogi_hind(kooginimi,moot))