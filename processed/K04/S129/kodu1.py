#pagarikoja kassaaparaat
import math


def koogi_hind(nimi, mõõt):
        if nimi == "šokolaadikook":
            return round(0.06*float(mõõt) * float(mõõt)*math.pi, 2)
        elif nimi == "ploomikook":
            return round(0.04*float(mõõt) * float(mõõt)*math.pi, 2)
        elif nimi == "Napoleoni kook":
            return round(0.10*float(mõõt) * float(mõõt), 2)
        
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud")
        

while True:
    nimetus = input("Sisesta koogi nimi: ")
    if nimetus == "":
        break
    suurus = input("Sisesta koogi mõõt: ")
    
    print("Koogi hind on", koogi_hind(nimetus, suurus), "eurot")
    

    
        
        
        

    
    
    

    
    
    
    
    
    
        