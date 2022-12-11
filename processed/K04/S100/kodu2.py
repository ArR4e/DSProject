def summa(u, v):
    c = 299792.458
    return (u+v)/(1+(u*v)/c**2)

esimene = float(input("Sisestage esimese keha kiirus: "))
teine = float(input("Sisestage teise keha kiirus: "))
kolmas = float(input("Sisestage kolmanda keha kiirus: "))
neljas = float(input("Sisestage neljanda keha kiirus: "))

print(f"Kiiruse summa on {summa(summa(summa(esimene, teine), kolmas), neljas)} km/h.")