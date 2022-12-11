from math import pi

def koogi_hind(nimi, mõõt=6):
        if nimi.lower() == "ploomikook":
            return(round(0.04*pi*mõõt**2, 2))
        elif nimi.lower() == "šokolaadikook":
            return(round(0.06*pi*mõõt**2, 2))
        elif nimi.lower() == "napoleoni kook":
            return(0.10*mõõt**2)
        else:
            raise Exception("vale sisend")

while True:
    nimi=input("Sisesta kooginimi: ")
    if nimi=="":
        break
    mõõt=float(input("Sisesta koogi suurus: "))    
    
    print(koogi_hind(nimi, mõõt))
