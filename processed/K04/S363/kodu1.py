def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        suurus = 3.14159 * float(mõõt)**2
        return round(0.06*suurus, 2)
    if nimi == "ploomikook":
        suurus = 3.14159 * float(mõõt)**2
        return round(0.04*suurus, 2)
    if nimi == "Napoleoni kook":
        suurus = float(mõõt)**2
        return round(0.1*suurus, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud")
    
nimi = "šokolaadikook"

while True:
    nimi = input("Mis on koogi nimi? ")
    
    if nimi == "":
        break
    
    else:
        mõõt = input("Mis on koogi mõõt? ")
    
        print(koogi_hind(nimi, mõõt))
    
