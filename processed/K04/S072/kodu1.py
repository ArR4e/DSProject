from math import pi

def koogi_hind(nimi, mõõt):
    andmebaas = {"šokolaadikook": 0.06, "ploomikook": 0.04, "Napoleoni kook": 0.10}
    
    if nimi not in andmebaas:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    if nimi == "Napoleoni kook":
        tulemus = mõõt ** 2 * andmebaas[nimi]
    else:
        tulemus = mõõt ** 2 * pi * andmebaas[nimi]
        
    return round(tulemus, 2)

while True:
    sisend_nimi = input("Sisestage koogi nimi: ")
    
    if sisend_nimi == '':
        break
    
    sisend_mõõt = float(input("Sisestage koogi mõõt: "))
    
    print(koogi_hind(sisend_nimi, sisend_mõõt))
    