import math

def koogi_hind(nimi, moot):
    if nimi != "šokolaadikook" or "ploomikook" or "Napoleoni kook":
            
        print("Sellist kooki andmebaasist ei leitud")
        
    else:
        if moot != float:
            pass
        else:
            moot = float(moot)
            if nimi == "šokolaadikook":

                cm2 = (moot * moot * math.pi)
                hind = (cm2 * 0.06)
            elif nimi == "ploomikook":
                
                cm2 = (moot * moot * math.pi)
                hind = (cm2 * 0.04)
            elif nimi == "Napoleoni kook":
                
                cm2 = (moot * moot)
                hind = (cm2 * 0.1)
            else:
                pass
            
            return round(hind, 2)


xmoot = None
xnimi = None
while xmoot or xnimi != "":
    xnimi = input("Sisestage koogi nimi:")
    xmoot = input("Sisestage koogi moot")
    print(koogi_hind(xnimi, xmoot))
   