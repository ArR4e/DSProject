from math import pi

def koogi_hind(ruut_cm_hind, pindala):
    return ruut_cm_hind * pindala

mõõt = float(input("Sisesta mõõt sentimeetrites:"))
nimi = input("Sisesta koogi nimi:")

if nimi == "šokolaadikook":
    ruut_cm_hind = 0.06
    pindala = ((mõõt**2) * pi)
    print("Sellise šokolaadikoogi hind on", round(koogi_hind(ruut_cm_hind, pindala), 3), "eurot.")
    
elif nimi == "ploomikook":
    ruut_cm_hind = 0.04 
    pindala = ((mõõt**2) * pi)
    print("Sellise ploomikoogi hind on", round(koogi_hind(ruut_cm_hind, pindala), 3), "eurot.")
    
elif nimi == "Napoleoni kook":
    ruut_cm_hind = 0.10
    pindala = (mõõt**2)
    print("Sellise Napoleoni koogi hind on", round(koogi_hind(ruut_cm_hind, pindala), 3), "eurot.")
        
else:
    print("Sellist kooki andmebaasist ei leitud.")
    
   
    

    