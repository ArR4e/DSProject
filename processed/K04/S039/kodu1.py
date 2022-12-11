from math import pi
def koogi_hind(kook,suurus):
    if kook=="šokolaadikook":
        return round(0.06*(suurus**2)*pi,2)
    elif kook=="ploomikook":
        return round(0.04*(suurus**2)*pi,2)
    elif kook=="Napoleoni kook":
        return round(0.1*suurus**2,2)
    else:
        raise Exception("Sellist kooki andmebaasis ei leidu")
        return "Sellist kooki andmebaasis ei leidu"

while True:
    kook=input("Millist kooki soovid tellida (šokolaadikook,ploomikook,Napoleoni kook)? ")
    if kook=="":
        break
    suurus=float(input("Millised on mõõtmed? "))
    hind=koogi_hind(kook,suurus)
    print("Koogi hind on "+str(round(hind,2))+" eurot.")
    print("--------------------------")

