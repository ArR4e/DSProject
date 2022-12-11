from math import pi
hind=0
nimi='x'
suurus=1
def koogi_hind(nimi, suurus):
    if nimi!='šokolaadikook' and nimi!='ploomikook' and nimi!='Napoleoni kook':
        print("Sellist kooki andmebaasist ei leitud")
    else:
        if nimi=='šokolaadikook':
            hind=round(pi*suurus**2*0.06,2)
        if nimi=='ploomikook':
            hind=round(pi*suurus**2*0.04,2)
        if nimi=='Napoleoni kook':
            hind=round(suurus**2*0.1,2)
        print(hind)
while True:
    nimi=input("Palun sisestage koogi nimi: ")
    if nimi=="":
        break
    suurus=float(input("Palun sisestage koogi suurus: "))
    koogi_hind(nimi, suurus)
    
        
        