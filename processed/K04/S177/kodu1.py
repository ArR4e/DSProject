from math import*
def koogi_hind(nimi, suurus):
    if nimi == "šokolaadikook":
        return round(0.06*(float(pi)*float(suurus)**2),2)
    elif nimi == "ploomikook":
        return round(0.04*(float(pi)*float(suurus)**2), 2)
    elif nimi == "Napoleoni kook":
        return round (0.10*float(suurus)**2, 2)
    else:
        raise Exception ("Sellist kooki andmebaasist ei leitud")
while True:
    nimi = input("Sisestage soovitud koogi nimi:")
    if nimi == "":
        break
    suurus = input ("Sisestage soovitud koogi suurus:")
    print ("Koogi hind on", koogi_hind(nimi, suurus), "eurot")