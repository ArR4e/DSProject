from math import pi

def koogi_hind(x, y):
    if x == "šokolaadikook":
        return round(pi*(koogi_mõõt**2)*0.06, 2)
    elif x == "ploomikook":
        return round(pi*koogi_mõõt**2*0.04, 2)
    elif x == "napoleoni kook":
        return round(koogi_mõõt**2*0.10, 2)
        
while True:       
    koogi_nimi = str(input("Sisestage koogi nimi: ")).lower()
    if koogi_nimi == "šokolaadikook" or koogi_nimi == "ploomikook"or koogi_nimi == "napoleoni kook":
        koogi_mõõt = float(input("Sisestage koogi mõõt: "))
        print(koogi_hind(koogi_nimi, koogi_mõõt)) 
    elif koogi_nimi == "":
       break
    else:
        print("Sellist kooki andmebaasist ei leitud")