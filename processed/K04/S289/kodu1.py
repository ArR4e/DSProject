from math import pi

def koogi_hind(nimi, suurus):
    if nimi == str("šokolaadikook"):
        return(round((pi * suurus ** 2 * 0.06), 2))
    elif nimi == str("ploomikook"):
        return(round((pi * suurus ** 2 * 0.04), 2))
    elif nimi == str("Napoleoni kook"):
        return(round((suurus ** 2 * 0.1), 2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
while True:
    nimi = str(input("Sisesta koogi nimi: "))
    if nimi == '':
        break
    suurus = float(input("Sisesta koogi külje pikkus või raadius: "))
    print(koogi_hind(nimi, float(suurus)))
