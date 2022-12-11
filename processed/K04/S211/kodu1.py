from math import pi
           
def koogi_hind(koogi_nimi, r):
    
    if koogi_nimi != "šokolaadikook" and koogi_nimi !="ploomikook" and koogi_nimi !="Napoleoni kook":
        raise Exception("Sisestatud kooki andmebaasist ei leitud :(")
        
    if koogi_nimi == 'šokolaadikook':
        ühiku_hind = 0.06
        kogu_hind = ühiku_hind*pi*r**2
        return round(kogu_hind, 2)

    elif koogi_nimi == 'ploomikook':
        ühiku_hind = 0.04
        kogu_hind = ühiku_hind*pi*r**2
        return round(kogu_hind, 2)
        
    
    elif koogi_nimi == 'Napoleoni kook':
        ühiku_hind = 0.10
        kogu_hind = r**2*ühiku_hind
        return round(kogu_hind, 2)


while True:
    
    koogi_nimi = str(input("Sisesta koogi nimi: "))
    
    
    if koogi_nimi == "":
        break
    else:
        r = float(input("Sisesta koogi raadius (cm): "))
        väljund = koogi_hind(koogi_nimi, r)
        print("Koogi hind on: ", väljund)
        
