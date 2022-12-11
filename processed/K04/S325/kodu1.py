from math import pi
kook = "kook"
def koogi_hind (kk,a):
    try:
        if kk == "šokolaadikook":
            return (0.06*a*a*pi/4)
        elif kk == "ploomikook":
            return (0.04*a*a*pi/4)
        elif kk == "Napoleoni kook":
            return (0.1*a*a)
    except:
        print("Sellist kooki andmebaasist ei leitud")
while True:
    kook = str(input("Mis kooki soovite?:"))
    if kook == "":
        break
    l = float(input("Kui suur on kook?:"))
    print("Teie",kook,"läheb maksma",round(koogi_hind(kook,l),2),"eurot.")