def summa(u, v):
    c = 299792.458
    return (u+v)/(1+((u*v)/c**2))

esimene_kiirus = float(input("Esimese keha kiirus: "))
teine_kiirus = float(input("Teise keha kiirus: "))
kolmas_kiirus = float(input("Kolmanda keha kiirus: "))
neljas_kiirus = float(input("Neljanda keha kiirus: "))

summa1 = summa(esimene_kiirus, teine_kiirus)
summa2 = summa(summa1, kolmas_kiirus)
summa3 = summa(summa2, neljas_kiirus)
print(f"Kiiruste summa on {summa3} km/h")

