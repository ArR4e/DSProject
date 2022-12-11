import math
def koogi_hind(knimi, kpikkus):
    if knimi == "šokolaadikook":
        hind = round(0.06*math.pi*kpikkus**2, 2)
        print(hind,"eurot")
    elif knimi == "ploomikook":
        hind = round(0.04*math.pi*kpikkus**2, 2)
        print(hind,"eurot")
    elif knimi == "Napoleoni kook":
        hind = round(0.10*kpikkus**2, 2)
        print(hind,"eurot")
    else:
        print("Sellist kooki andmebaasist ei leitud")
        
while True:
    knimi = str(input("Sisesta oma kook "))
    if len(knimi) == 0:
        break
    kpikkus = float(input("Sisesta oma koogipikkus(cm) "))
    koogi_hind(knimi, kpikkus)