from math import pi
def koogi_hind(nimi, moot):
    maksumus = 0
    suurus = 0
    erand = "Sellist kooki andmebaasist ei leitud."
    if nimi == "šokolaadikook":
        suurus = pi * moot ** 2 
        maksumus = suurus * 0.06
    elif nimi == "ploomikook":
        suurus = pi * moot ** 2 
        maksumus = suurus * 0.04
    elif nimi == "Napoleoni kook":
        suurus = moot ** 2
        maksumus = suurus * 0.10
    else:
        return erand
    return round(maksumus,2)

while True:
    moot = 0
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "šokolaadikook" or nimi == "ploomikook" or nimi == "Napoleoni kook":
        moot = float(input("Sisesta koogi mõõt: "))
        print(f"Koogi maksumus on {koogi_hind(nimi, moot)} eurot.")
    elif nimi == '':
        
        break
    else:
        print(koogi_hind(nimi, moot))
    
    
        

    
    
    