from math import pi

#sokolaadikoogi_hind = 0.06
#ploomikoogi_hind = 0.04
#napoleonikoogi_hind = 0.10

def koogi_hind(nimi,moot):
    if nimi =="šokolaadikook":
        hind = 0.06
        pindala = (pi*moot**2)
        sokolaadikoogi_hind = (hind*pindala)
        sokolaadikoogi_hind = round (sokolaadikoogi_hind,2)
        return (sokolaadikoogi_hind)
    elif nimi == "ploomikook":
        hind = 0.04
        pindala = (pi*moot**2)
        ploomikoogi_hind = (hind*pindala)
        ploomikoogi_hind = round (ploomikoogi_hind,2)
        return (ploomikoogi_hind)
    elif nimi == "Napoleoni kook":
        hind = 0.10
        pindala = moot**2
        napoleonikoogi_hind = (hind*pindala)
        napoleonikoogi_hind = round (napoleonikoogi_hind,2)
        return (napoleonikoogi_hind)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud!")
    
while True:
    nimi = (input("Sisesta kooginimi:"))
    if nimi == "":
            break
    if nimi == "šokolaadikook" or nimi == "ploomikook" or nimi == "Napoleoni kook":
            try:
                moot = float(input("Sisesta koogimõõt, kas külg või raadius"))
                hind = koogi_hind(nimi,moot)
                print (hind)
                print ("Koogi hind on","{:,.2f}".format (hind),"eurot.")
            except ValueError as e:
                print(e.args[0])
    else:
            print ("Sellist kooki andmebaasist ei leitud!")