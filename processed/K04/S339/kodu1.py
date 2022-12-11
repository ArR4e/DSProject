from math import pi

def koogi_hind(nimi, suurus):
    if nimi == "šokolaadikook":
        return round(0.06*suurus**2*pi, 2)
    elif nimi == "ploomikook":
        return round(0.04*suurus**2*pi, 2)
    elif nimi == "Napoleoni kook":
        return round(0.10*suurus**2, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == " ":
        break
    suurus = float(input("Sisesta suurus:"))
    print(koogi_hind(nimi, suurus))