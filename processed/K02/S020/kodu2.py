import math
liinipikkus = int(input("Palun sisesta liini pikkus meetrites: "))
maksimaalkaugus = int(input("Palun sisesta liini postivahe maksimaalkaugus: "))

postide_minimaalarv = round(liinipikkus/maksimaalkaugus, 0+1)
postide_minimaalarv = math.ceil(postide_minimaalarv)

if liinipikkus > maksimaalkaugus:
    print ("Liini ehitamiseks on vaja minimaalselt" + str(postide_minimaalarv)+ "posti.")
if liinipikkus == maksimaalkaugus:
    print("Liini ehitamiseks on vaja minimaalselt" + str(postide_minimaalarv) + "posti")

if liinipikkus < maksimaalkaugus:
    print ("Liini ehitamiseks on vaja minimaalselt" + str(postide_minimaalarv)+ "posti.")    
