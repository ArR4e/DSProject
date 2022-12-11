import math

pikkus = int(input("Sisesta liini pikkus (m): "))
kaugus = int(input("Sisesta kõrvutiseisvate postide maksimaalkaugus (m): "))

poste_kokku = math.ceil(pikkus / kaugus + 1)

print("Vaja minevaid poste on", poste_kokku)