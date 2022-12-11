from math import pi
#funktsioon
def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        maksumus = round(mõõt**2 * pi * 0.06, 2)
        return(maksumus)
    elif nimi == "ploomikook":
        maksumus = round(mõõt**2 * pi * 0.04, 2)
        return("kook maksab", maksumus)
    elif nimi == "Napoleoni kook":
        maksumus = round(mõõt**2 * 0.10, 2)
        return("kook maksab", maksumus)
    elif nimi != "Napoleoni kook" or nimi != "ploomikook" or nimi != "šokolaadikook":
        return("Sellist kooki andmebaasist ei leitud.")
                
#suhtlus kasutajaga + loop

while True:
    nimi = input("mis kooki te soovite? ")
    if nimi == "":
        break 
    mõõt = float(input("Kui suur kook on? "))
    #print("Koogi hind on {}".format(koogi_hind(nimi, mõõt)))
    