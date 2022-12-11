from math import pi

def koogi_hind(nimi, mõõt):
    if nimi != "šokolaadikook" and nimi != "ploomikook" and nimi != "Napoleoni kook" and nimi != "":
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    if nimi == "šokolaadikook":
        pindala = float(pi * (float(mõõt))**2)
        hind = float(pindala * 0.06)
        hindround = round(hind, 2)
        print("Küsitud kook maksab " + str(hindround) + " eurot.")
        
    if nimi == "ploomikook":
        pindala = float(pi * (float(mõõt))**2)
        hind = float(pindala * 0.04)
        hindround = round(hind, 2)
        print("Küsitud kook maksab " + str(hindround) + " eurot.")
        
    if nimi == "Napoleoni kook":
        pindala = float((float(mõõt))**2)
        hind = float(pindala * 0.10)
        hindround = round(hind, 2)
        print("Küsitud kook maksab " + str(hindround) + " eurot.")
     
    if nimi == "":
        exit()

while True:
    y = input("Koogi nimi: ")
    x = input("Koogi mõõt: ")
    koogi_hind(y, x)
        