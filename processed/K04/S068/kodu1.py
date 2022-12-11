from math import pi

def koogi_hind(mõõt,hind):
    makse=hind*mõõt
    return round(makse,2)

while True:
    a=str(input("Sisestage koogi nimi: "))
    if a=="":
        break
    b=float(input("Sisestage koogi mõõt: "))
    mõõt=0
    hind=0
    try:
        if a == str("šokolaadikook"):
            hind = float(0.06)
            suurus= b**2*pi
            print((str(koogi_hind (suurus,hind)))+str("€"))
        elif a == str("ploomikook"):
            hind = float(0.04)
            suurus= b**2*pi
            print((str(koogi_hind(suurus,hind)))+str("€"))    
        elif a == str("Napoleoni kook"):
            hind = float(0.10)
            suurus= b*b
            print((str(koogi_hind(suurus,hind)))+(str("€")))       
    except:
        print("Sellist kooki andmebaasist ei leitud")


