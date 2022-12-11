pikkus = int(input("Sisestage liini pikkus meetrites: "))
maksimum = int(input("Sisestage maksimaalne postide vaheline kaugus: "))

postide_arv = int(pikkus // maksimum + 1)
if postide_arv == 1:
    postide_arv += 1
print("Vaja läheb ", postide_arv, " posti.")