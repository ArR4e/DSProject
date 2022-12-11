import math
liini_pikkus = int(input("Palun sisesta liini pikkus: "))
maksimaalkaugus = int(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugus: "))
postide_arv = float(liini_pikkus / maksimaalkaugus) +1

if maksimaalkaugus > liini_pikkus:
    print(2)
else:
    print(int(math.ceil(postide_arv)))