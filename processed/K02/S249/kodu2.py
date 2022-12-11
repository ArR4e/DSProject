import math

pikkus = int(input("Kui pikk on elektriliin? "))
max_kaugus = int(input("Mis on maksimaalne kaugus kõrvutiasetsevate postide vahel? "))

print(int(math.ceil(pikkus / max_kaugus + 1)))
