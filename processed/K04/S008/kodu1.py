from math import pi

def koogi_hind (koogid, mõõdud):
    if koogid == "šokolaadikook":
        return round((mõõdud**2 * pi) * 0.06, 2)
    
    elif koogid == "ploomikook":
        return round((mõõdud**2 * pi) * 0.04, 2)
    
    elif koogid == "Napoleoni kook" or koogid == "napoleoni kook":
        return round((mõõdud**2) * 0.1, 2)
    
        
while True:

    koogid = input("Sisestage soovitav kook: ")
    if koogid == "":
        break
    elif koogid != "šokolaadikook" and koogid != "ploomikook" and koogid != "Napoleoni kook" and koogid !="napoleoni kook":
        print ("Sellist kooki meie menüüs ei ole!")
    else:
        mõõdud = float(input ("Sisestage soovitava koogi mõõt: "))
        
        print (koogi_hind(koogid, mõõdud))