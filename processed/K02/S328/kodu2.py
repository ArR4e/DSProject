import math
liin = int(input("Mis liini pikkus on?"))
kaugus = int(input("Mis kõrvutiasetsevate postide maksimaalkaugus on?"))
if kaugus > liin:
    print(2)
else:
    print(math.ceil(liin/kaugus)+1)