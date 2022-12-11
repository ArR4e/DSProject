def summa(u, v):
    return (u+v)/((u*v)/(299792.458*299792.458)+1)

kiirus1 = float(input("Sisesta esimese objekti kiirus: "))
kiirus2 = float(input("Sisesta teise objekti kiirus: "))
kiirus3 = float(input("Sisesta kolmanda objekti kiirus: "))
kiirus4 = float(input("Sisesta neljanda objekti kiirus: "))

teine = summa(kiirus1, kiirus2)
kolmas = summa(teine, kiirus3)
neljas = summa(kolmas, kiirus4)

print("Kiiruste summa on", neljas)