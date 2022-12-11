from math import pi
def koogi_hind(nimi,suurus):
    if nimi == "šokolaadikook":
        return round(0.06*pi*float(suurus**2))
    elif nimi == "ploomikook":
        return round(0.04*pi*float(suurus**2))
    elif nimi == "Napoleoni kook":
        return round(0.10*float(suurus)*float(suurus))
     else:
         raise Exception ("Sellist kooki andmebaasist ei leitud")
    
while True:    
    nimi = str(input("Mis on koogi nimi?"))
    if nimi == "":
        break
    suurus = float(input("Mis on koogi suurus?"))
    print("Koogi hind on", koogi_hind(nimi,suurus), "eurot.")