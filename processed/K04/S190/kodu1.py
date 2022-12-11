from math import pi

s = 0.06
p = 0.04
n = 0.1

def koogi_hind(nimi,mõõt):
    if nimi != "šokolaadikook" and nimi != "ploomikook" and nimi != "Napoleoni kook":
        raise Exception("Sellist kooki andmebaasist ei leitud!")

    if nimi == "šokolaadikook":
        return float(round(pi*(mõõt)**2*s,2))
    
    elif nimi == "ploomikook":
        return float(round(pi*(mõõt)**2*p,2))
    
    elif nimi == "Napoleoni kook":
        return float(round(mõõt**2*n,2))

while True: 
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõt: "))
            
    
    print(str(koogi_hind(nimi,mõõt))+" €")
    

