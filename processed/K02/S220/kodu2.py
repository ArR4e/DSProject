import math

liini_pikkus = int(input("Sisestage liini pikkus "))
max_kaugus = int(input("Sisestafe postide maksimaalkaugus "))
vahe = math.ceil(liini_pikkus/max_kaugus) + 1
if liini_pikkus < max_kaugus :
    print("Liini ehitamiseks läheb vaja 2 posti")
else :
    print("Liini ehitamiseks läheb vaja", int(vahe), "posti")


    
