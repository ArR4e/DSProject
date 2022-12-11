from math import pi
    
def koogi_hind(nimi, moot):
    if nimi == "šokolaadikook" or nimi == "ploomikook":
        S = moot**2*pi
        if nimi == 'šokolaadikook':
            hind = 0.06
            return round(hind*S,2)
        else:
            hind = 0.04
            return round(hind*S,2)
    elif nimi == "Napoleoni kook":
        S = moot**2
        hind = 0.10
        return round(hind*S,2)
    else:
        raise Exception ('Sellist kooki andmebaasist ei leitud')

    
while True:
    nimi = input('Mis on koogi nimi?')
    if nimi == '':
        break
    else:
        moot = float(input('Mis on koogi mõõt?'))
        print("Koogi hind on", koogi_hind(nimi, moot), "eurot.")
