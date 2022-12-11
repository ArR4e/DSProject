from math import pi
nimi = str(input("Sisestage soovitud koogi nimi: "))
mõõtmed = float(input("Sisestage soovitud koogi suurus: "))


    
def koogi_hind(nimi, mõõtmed):
    while True:
        if nimi != "šokoladikook" and nimi != "ploomikook" and nimi != "Napoleoni kook":
            print("Sellist kooki andmebaasist ei leitud.")
            break
        else:
            if nimi == "šokoladikook" or nimi == "ploomikook":
                pindala = pi*mõõtmed**2
                if nimi == "šokoladikook":
                    hind = round(pindala * 0.06, 2)
                    print(hind)
                    break
                else:
                    hind = round(pindala * 0.04, 2)
                    print(hind)
                    break
            else:
                pindala = mõõtmed**2
                hind = round(pindala * 0.1, 2)
                print(hind)
                break

    
    
        

koogi_hind(nimi, mõõtmed)
        