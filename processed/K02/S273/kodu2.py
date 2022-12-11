liini_pikkus = int(input("Kui pikk on elektriliin? "))

max_kaugus = int(input("Mis on maksimaalne postide vaheline kaugus? "))

print("Minimaalselt on vaja ", int(liini_pikkus / max_kaugus) + 1)