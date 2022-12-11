from math import pi
šokolaadikook=0.06
ploomikook=0.04
Napoleoni_kook=0.1

def koogi_hind(nimi, mõõt):
    if nimi=="Napoleoni kook":
        nimi="Napoleoni_kook"
    try:
        nimi=globals()[nimi]
    except:
        raise Exception ("Sellist kooki andmebaasist ei leitud")
     #   print("Sellist kooki andmebaasist ei leitud")
        return
    if(nimi==0.1):
        return(round(nimi*mõõt*mõõt,2))
    else:
        return(round(nimi*pi*mõõt*mõõt,2))
while True:
    nimi=str(input("Sisestage koogi nimi: "))
    if not nimi:
        break
    mõõt=float(input("Sisestage koogi mõõt sentimeetrites: "))
    if koogi_hind(nimi,mõõt):
        print("Koogi hind on",str(koogi_hind(nimi,mõõt))+"€")