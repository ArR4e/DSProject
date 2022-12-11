from math import pi
nimi = input("Sisesta koogi nimi: ")
mõõt = float(input("Sisesta koogi mõõt: "))
def koogi_hind(nimi, mõõt):
    while True:
        if (nimi == "šokolaadikook"):
            return (round(mõõt**2*pi*0.06, 2))
        elif (nimi == "ploomikook"):
            return (round(mõõt**2*pi*0.04, 2))
        elif (nimi == "Napoleoni kook"):
            return (round(mõõt**2*0.1, 2))
        elif (nimi == ""):
            break
        else:
            raise ValueError("Sellist kooki ei leitud")
        
