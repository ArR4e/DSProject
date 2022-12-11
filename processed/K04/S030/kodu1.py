from math import pi
nimi = input("Sisesta koogi nimi: ")
nimi = nimi.lower()
moot = float(input("Sisesta koogi raadius või küljepikkus cm: "))

def koogi_hind(nimi, moot):
    while True:
        if nimi == "šokolaadikook":
            return round((0.06*pi*moot**2), 2)
        elif nimi == "ploomikook":
            return round((0.04*pi*moot**2), 2)
        elif nimi == "napoleoni kook":
            return round((0.1*moot**2), 2)
        else:
            raise ValueError('Sellise nimega kooki andmebaasis ei ole')

        if nimi == '':
            break
        
print("Koogi hind on", koogi_hind(nimi, moot), "eurot.")


   


        