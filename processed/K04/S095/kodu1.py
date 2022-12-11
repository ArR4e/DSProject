import math
while True:
    koogi_nimi= input("Palun sisesta koogi nimi: ")
    mõõt= input("Palun sisesta koogi mõõtmed: ")
    if koogi_nimi != "":
        break     
def koogi_hind(koogi_nimi, mõõt):    
        if koogi_nimi == 'šokolaadikook':
            return round((math.pi*(float(mõõt)**2)*0.06), 2)
        elif koogi_nimi == 'ploomikook':
            return round((math.pi*(float(mõõt)**2)*0.04), 2)
        elif koogi_nimi == 'Napoleoni kook':
            return round(((float(mõõt)**2)*0.10), 2)
        else:
            raise ValueError ('Sellist kooki andmebaasist ei leitud')

print("Sinu koogi maksumus on", koogi_hind(koogi_nimi, mõõt) , "eurot.")