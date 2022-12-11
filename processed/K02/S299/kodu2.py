import math

liini_pikkus = int(input("Sisestage liini pikkus meetrites: "))

postide_kaugus = (int(input("Sisestage maksimaalne postide vaheline kaugus meetrites: ")))

minimaalne_postide_arv = (liini_pikkus / postide_kaugus + 1)

print(math.ceil(minimaalne_postide_arv))