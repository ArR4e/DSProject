import math
pikkus = float(input("Sisesta elektriliini pikkus: "))
kaugus = float(input("Sisesta postidevaheline maksimaalkaugus: "))
arv = pikkus/kaugus + 1
if arv >= 2:
    print ("Liini ehitamiseks on minimaalselt vaja", math.ceil(arv), "posti")
else:
    print(2)

