from math import pi
def koogi_hind(koogi_nimi,mõõt):
    if koogi_nimi.lower() == 'šokolaadikook':
        return(round((((float(mõõt)**2)*pi)*0.06),2))
    elif koogi_nimi.lower() == 'ploomikook':
        return(round((((float(mõõt)**2)*pi)*0.04),2))
    elif koogi_nimi.capitalize() == 'Napoleoni kook':
        return(round((((float(mõõt)**2))*0.10),2))
    else:
        print('Sellist kooki andmebaasist ei leitud')

koogi_nimi = input()

while koogi_nimi != "":
    mõõt = (input())
    koogi_hind(koogi_nimi,mõõt)
    koogi_nimi = input()
    continue
if koogi_nimi == "":
    quit