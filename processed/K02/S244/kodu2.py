import math

liini_pikkus = int(input("Sisesta liini pikkus: "))
kõrvutiasetsevate_postide_maksimaalkaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus: "))
postide_arv = (liini_pikkus/kõrvutiasetsevate_postide_maksimaalkaugus)+1
x = math.ceil(postide_arv)
if liini_pikkus < kõrvutiasetsevate_postide_maksimaalkaugus:
    print(2)
else:
    print(x)