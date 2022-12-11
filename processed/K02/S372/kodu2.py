import math
liinipikkus = int(input("Sisestage liini pikkus: "))
maksimaalkaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))
postide_arv = (math.ceil(liinipikkus / maksimaalkaugus)) + 1
print(postide_arv)
