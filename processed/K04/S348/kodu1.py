from math import pi

def koogi_hind(nimi, mõõtmed):
    if nimi == "šokolaadikook":
        return(round(pi*(mõõtmed**2)*0.06,2))
    elif nimi == "ploomikook":
        return(round(pi*(mõõtmed**2)*0.04,2))
    elif nimi == "Napoleoni kook":
        return(round((mõõtmed**2)*0.10,2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
    
while True:
    kooginimi = input("Sisestage koogi nimi: ")
    if kooginimi != "":
        koogimõõt = float(input("Sisestage koogi mõõt: "))
        print("Koogi hind on", koogi_hind(kooginimi, koogimõõt),"eurot")
    else:
        break

            
        
        