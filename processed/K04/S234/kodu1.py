from math import pi
def koogi_hind(nimi,mõõt):
    if nimi=="Napoleoni kook":
        hind=round(float(mõõt)**2*0.10,2)
        return(hind)
    elif nimi=="šokolaadikook"or nimi=="ploomikook":
        if nimi=="šokolaadikook":
            hind=round(float(mõõt)**2*pi*0.06,2)
            return(hind)
        else:
            hind=round(float(mõõt)**2*pi*0.04,2)
            return(hind)
    else:
        hind="Sellist kooki andmebaasist ei leitud"
        return(hind)
while True:
    nimi=input("koogi nimi")
    if len(nimi)==0:
        break
    suurus=float(input("koogi suurus"))
    print(koogi_hind(nimi,suurus))