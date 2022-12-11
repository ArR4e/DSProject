def summa(u, v):
    c = 299792.458
    return (float(u) + float(v))/(1 + ((float(u) * float(v)) / c ** 2))

u = input("Sisesta esimese keha kiirus vaatleja suhtes: ")
v = input("Sisesta teise keha kiirus esimese keha suhtes: ")
x = input("Sisesta kolmanda keha kiirus teise keha suhtes: ")
y = input("Sisesta neljanda keha kiirus kolmanda keha suhtes: ")

kiiruste_summa = summa(summa(summa(u, v), x), y)

print("Nende kiiruste summa on " + str(kiiruste_summa) + " km/h.")