import math

nimi = input("Sisesta siia kooginimi: ")
summa = 0

def koogi_hind(nimi, moot):
    if nimi == "šokolaadikook":
        pindala = math.pi * moot * moot
        return round((pindala * 0.06), 2)
    elif nimi == "ploomikook":
        pindala = math.pi * moot * moot
        return round((pindala * 0.04), 2)
    elif nimi == "Napoleoni kook":
        pindala = moot * moot
        return round((pindala * 0.10), 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while nimi != "":
    moot = float(input("Sisesta siia moot: "))
    try:
        print(koogi_hind(nimi, moot))
    except:
        print('Sellist kooki andmebaasist ei leitud')
        
    nimi = input("Sisesta siia kooginimi: ")
    

        




