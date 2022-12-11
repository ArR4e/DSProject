def summa(u, v):
    kiirus = 0
    kiirus = (u + v)/(1 + (u * v)/299792.458**2)
    return kiirus

kiirus1 = float(input("Esimese keha kiirus vaatleja suhtes: "))
kiirus2 = float(input("Teise keha kiirus esimese suhtes: "))
kiirus3 = float(input("Kolmanda keha kiirus teise suhtes: "))
kiirus4 = float(input("Neljanda keha kiirus kolmanda suhtes: "))
v_kiirus2 = summa(kiirus1, kiirus2)
v_kiirus3 = summa(v_kiirus2, kiirus3)
v_kiirus4 = summa(v_kiirus3, kiirus4)
print("Kiiruste summa on: ", v_kiirus4, "km/s")