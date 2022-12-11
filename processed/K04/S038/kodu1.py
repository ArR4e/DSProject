from math import pi
tyyp=0
suurus=0
hind=0
def koogi_hind(a,b):
    while True:
        a=input("Mis kooki te soovite?(šokolaadikook/ploomikook/Napoleoni kook): ")   
        if str(a)=="":
            break
        else:
            b=(input("Sisestage koogi raadius/kylje pikkus:"))
            if str(a)== "šokolaadikook":
                hind= round((0.06*pi*(float(b)*float(b))),2)
            elif str(a)== "ploomikook":
                hind=round((0.04*pi*(float(b)*float(b))),2)
            elif str(a)=="Napoleoni kook":
                hind=round((0.1*(float(b)*float(b))),2)
            else:
                raise ValueError("Sellist kooki andmebaasist ei leitud.")
            return hind
print(koogi_hind(tyyp,suurus))
        