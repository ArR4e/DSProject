import math
liinipikkus = int(input("Sisestage liini pikkus: ")) 
kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))
arv = float(liinipikkus / kaugus) + 1

if kaugus > liinipikkus:
    print(2)
else:
    print(int(math.ceil(arv)))