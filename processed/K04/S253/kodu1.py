from math import pi
def koogi_hind(koogi_nimi, moot):
    hind = 0
    pindala = 0

    if koogi_nimi == "šokolaadikook":
        pindala = pi*(moot**2)
        hind = pindala * 0.06
    elif koogi_nimi == "ploomikook":
        pindala = pi*(moot**2)
        hind = pindala * 0.04
    elif koogi_nimi == "Napoleoni kook":
        pindala = moot**2
        hind = pindala * 0.10
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    return round(hind, 2)
while True:
    try:
        ans1 = input("Sisestage koogi nimi: ")
        if ans1 == "":
            break
        ans2 = float(input("Sisestage koogi mõõt: "))
        print("Koogi hind on " + str(float(koogi_hind(ans1,ans2))) + " eurot.")
    except:
        print("Sellist kooki andmebaasist ei leitud")


        


