from math import pi

napoleoni_hind= 0.1
ploomi_hind= 0.04
šokolaadi_hind= 0.06

def koogi_hind(x, y,):
     
    
    
    if x == "Napoleoni kook":
        return(round(y*y*napoleoni_hind,2))
    elif x=="ploomikook":
        return(round(ploomi_hind*pi*y*y,2))
    elif x=="šokolaadikook":
        return(round(šokolaadi_hind*pi*y*y,2))
    elif x!="Napoleoni kook" and x!="ploomikook" and x!="šokolaadikook":
        raise Exception(print('Sellist kooki andmebaasis ei leitud'))
    
    
while True: 
    a=str(input('Mis kooki soovid? '))
    if a == "":
        break
    b=float(input("Sisesta koogi suurus sentimeetrites: "))
    print('Koogi hind on' +str(koogi_hind(a,b))+'€')

