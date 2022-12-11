import math
pikkus=int(input("sisesta liini pikkus:"))
maks= int(input("sisesta postide maksimaalne kaugus:"))
if pikkus<maks or pikkus==maks:
    
    print("Liini ehitamiseks on vaja minimaalselt 2 posti")
elif pikkus>maks:
        maxvahega=math.ceil(1+(pikkus/maks))
        print("Liini ehitamiseks on tarvis minimaalselt", str(maxvahega),"posti.")
