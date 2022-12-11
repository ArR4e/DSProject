import math

L = int(input("Sisestage liini pikkus: "))
Max = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))
V = math.ceil(L / Max) + 1

print(f"Poste läheb minimaalselt vaja:{V}")