from math import pi

def koogi_hind(nimi,mõõt):
     
    if nimi != "šokolaadikook" and  nimi != "ploomikook" and  nimi != "Napoleoni kook":
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    if nimi == "šokolaadikook":
        hind = 0.06*pi*float(mõõt)**2 #eurot
    elif nimi == "ploomikook":
        hind = 0.04*pi*float(mõõt)**2
    elif nimi == "Napoleoni kook":
        hind = 0.10*float(mõõt)**2
    
    return round(hind,2)



while True:
    Nimi = input("palun sisesta siia koogi nimi")
    if Nimi == "":
        break
    Mõõt = input("palun sisesta siia koogi mõõt")
    print(koogi_hind(Nimi,Mõõt))








    