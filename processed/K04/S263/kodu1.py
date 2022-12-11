from math import pi

while True:
    nimi = input("Sisesta kooginimi")
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogimõõt"))
    
    def koogi_hind(nimi, mõõt):
        if nimi == "šokolaadikook":
            return(round(0.06 * mõõt * mõõt * pi, 2))
        elif nimi == "ploomikook":
            return(round(0.04 * mõõt * mõõt * pi, 2))    
        elif nimi == "Napoleoni kook":
            return(round(0.10 * mõõt * mõõt, 2))
        else:
            raise ValueError("Sellist kooki andmebaasist ei leitud")
               
        
    print(koogi_hind(nimi,mõõt))
    
#šokolaadikook = 0.06 * mõõt * pi
#šokolaadikoogi_hind = koogi_hind
#ploomikoogi_hind = koogi_hind
#napoleonikoogi_hind = koogi_hind

#print(round(koogi_hind(nimi,mõõt), 2))         

    #ploomikook
    
    #napoleoni kook
    
    