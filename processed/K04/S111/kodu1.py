from math import pi

def koogi_hind(kook, suurus):
    if kook== "ploomikook":
        hind=round((suurus**2 * pi) * 0.04, 2)
        return print(hind)
    elif kook== "šokolaadikook":
        hind=round((suurus**2 * pi) * 0.06, 2)
        return print(hind)
    elif kook=="Napoleoni kook":
        hind=round(suurus**2 * 0.1, 2)
        return print(hind)
    else:
        return print("Sellist kooki meil andmebaasis pole")
    
while 1<2:
    kook= input("Sisestage koogi nimi: ")
    if kook=="":
        break
    else:
        suurus= float(input("Sisestage koogi suurus: "))
        koogi_hind(kook, suurus)
    
    