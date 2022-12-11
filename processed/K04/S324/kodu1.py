from math import*

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = round(((mõõt**2)*pi)*0.06, 2)
    elif nimi == "ploomikook":
        hind = round(((mõõt**2)*pi)*0.04, 2)
    elif nimi == "Napoleoni kook":
        hind = round((mõõt*mõõt)*0.1, 2)
    return hind

while True:
    nimi = input("Palun sisestage koogi nimi: ")
    if nimi == "":
        break
    
    else:
        try:
            mõõt = float(input("Palun sisestage koogi mõõt: "))
            print("Koogi maksumus on" , koogi_hind(nimi, mõõt) , "eurot.")
        except:
            print("Sellist kooki andmebaasist ei leitud")