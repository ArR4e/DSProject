from math import *
koogid=['šokolaadikook','ploomikook','Napoleoni kook']
def koogi_hind(nimi, moot):
    global nimi1
    if nimi not in koogid:
        raise Exception('Sellist kooki andmebaasist ei leitud')
    if nimi=='šokolaadikook':
        return(round(pi*(moot**2)*0.06,2))
    elif nimi== "ploomikook":
        return(round(pi*(moot**2)*0.04,2))
    elif nimi== "Napoleoni kook":
        return(round(0.1*(moot**2),2))
    nimi1=nimi

while True:
    nimi=input("Sisestage koogi nimi: ")
    if nimi=="":
        break
    moot=float(input("Sisestage koogi mõõt:"))
    print(koogi_hind(nimi, moot))
    

    
        