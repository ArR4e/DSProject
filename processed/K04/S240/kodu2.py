def summa(u, v):
    return (u + v)/(1+((u*v)/299792.458**2))

kiirus1 = float(input("Sisesta esimese keha kiirus vaatleja suhtes: "))
kiirus2 = float(input("Sisesta teise keha kiirus esimese suhtes: "))
kiirus3 = float(input("Sisesta kolmanda keha kiirus teise suhtes: "))
kiirus4 = float(input("Sisesta neljanda keha kiirus kolmanda suhtes: "))

k1 = summa(kiirus1, kiirus2)
k2 = summa(k1, kiirus3)
k3 = summa(k2, kiirus4)

print("Kõikide kiiruste summa on: " + str(k3) + " km/s")
