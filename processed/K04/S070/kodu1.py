import math
def koogi_hind(kook, suurus):
    try:
        if kook == "šokolaadikook":
            suurus = suurus**2 * math.pi #Kui on ringikujuline.
            return round(suurus * 0.06, 2)
        if kook == "ploomikook":
            suurus = suurus**2 * math.pi #Kui on ringikujuline.
            return round(suurus * 0.04, 2)
        if kook == "Napoleoni kook":
            suurus = suurus**2 #Kui on ruut.
            return round(suurus * 0.10, 2)
        if kook != "šokolaadikook" and kook != "ploomikook" and kook != "Napoleoni kook":
            raise Exception("Sellist kooki andmebaasist ei leitud")
    except:
        print("Sellist kooki andmebaasist ei leitud")
while True:
    kook = str(input("Sisestage koogi tüüp "))
    if kook == "":
            break
    suurus = float(input("Sisestage koogi suurus "))
    if koogi_hind(kook, suurus) == None:
        continue
    print("Koogi hind on", koogi_hind(kook, suurus), "eurot")
    
