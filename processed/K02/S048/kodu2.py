import math

liini_pikkus = int(input("Sisestage elektriliini pikkus: "))
mastide_kaugus = int(input("Sisestage mastide max kaugus üksteisest: "))

x = liini_pikkus / mastide_kaugus

if liini_pikkus == mastide_kaugus:
    print(2, "posti on vaja minimaalseselt, et ehitada antud elektriliin")
if mastide_kaugus == 1:
    print(math.floor(x)+1, "posti on vaja minimaalseselt, et ehitada antud elektriliin")
else:
    print(math.floor(x)+2, "posti on vaja minimaalseselt, et ehitada antud elektriliin")