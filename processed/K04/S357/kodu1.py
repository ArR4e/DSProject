from math import pi

def koogi_hind(nimi, suurus):
    if nimi.lower() == "ðokolaadikook":
        return round(0.06 * pi * suurus**2, 2)
    elif nimi.lower() == "ploomikook":
        return round(0.04 * pi * suurus**2, 2)
    elif nimi.lower() == "napoleoni kook":
        return round (0.1 * suurus * suurus, 2)
    else: raise Exception("Sellist kooki andmebaasist ei leitud")

try:
    while True:
        nimi = input("Sisesta koogi nimi: ")
        
        if nimi == "":
            break    
        
        suurus = float(input("Sisesta koogi mõõt: "))

        print("Koogi hind on", koogi_hind(nimi, suurus), "€")

except Exception as viga:
    print(viga)