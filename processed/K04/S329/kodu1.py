from math import pi

print("Tere, kallis kasutaja!")

def koogi_hind(nimi, mõõt):
    if mõõt <= 0:
        raise ValueError("Mõõt peab olema mittenegatiivne ja suurem kui null.")
    elif nimi == str("šokolaadikook"):
        pindala = pi * mõõt**2
        return round(0.06 * pindala, 2)
    elif nimi == str("ploomikook"):
        pindala = pi * mõõt**2
        return round(0.04 * pindala, 2)
    elif nimi == str("Napoleoni kook"):
        pindala = mõõt**2
        return round(0.10 * pindala, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
            
while True:
    nimi = str(input("Palun kirjutage koogi nimi: "))
    if nimi == str(""):
        break
    try:
        mõõt = float(input("Palun kirjutage koogi pikkus/raadius (cm): "))
        print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot.")
    except Exception as a:
        print(a)
