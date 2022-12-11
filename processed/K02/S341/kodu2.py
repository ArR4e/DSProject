import math
liini_pikkus = float(input("Sisestage liinipikkus: "))
maksimaalkaugus= float(input("Sisestage maksimaalkaugus: "))
esimenekomplekt = print(maksimaalkaugus/liini_pikkus)
teinekomplekt = print(math.ceil(maksimaalkaugus/liini_pikkus))
kolmaskomplekt = print(math.floor(maksimaalkaugus/liini_pikkus))