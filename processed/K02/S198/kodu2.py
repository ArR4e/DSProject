import math

liini_pikkus = int(input("Liini pikkus: "))
max_kaugus = int(input("Maksimaalne kaugus: "))

poste = max(math.ceil(liini_pikkus / max_kaugus) + 1, 2)
print("Poste on vaja:", poste)