from math import*

def koogi_hind(nimi, moot):
    
    if nimi == "šokolaadikook":
        pindala = pi*(moot**2)
        summa = round(pindala*0.06, 2)
        return(summa)
    
    if nimi == "ploomikook":
        pindala = pi*(moot**2)
        summa = round(pindala*0.04, 2)
        return(summa)
    if nimi == "Napoleoni kook":
        pindala = moot**2
        summa = round(pindala*0.10, 2)
        return(summa)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi !="":
        
            
        moot = float(input("Sisesta koogi mõõt:"))
        print(koogi_hind(nimi, moot))
    else:
        break
    

        
    