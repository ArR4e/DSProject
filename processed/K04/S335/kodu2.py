def summa(u, v):
    return (u + v) / (1 +(u * v / 299792.458 ** 2))

kiirus1 = float(input("Sisestage esimese keha kiirus (km/s): "))
kiirus2 = float(input("Sisestage teise keha kiirus (km/s): "))
kiirus3 = float(input("Sisestage kolmanda keha kiirus (km/s): "))
kiirus4 = float(input("Sisestage neljanda keha kiirus (km/s): "))

print("Kiiruste summa on: " + str(summa(summa(summa(kiirus1, kiirus2), kiirus3), kiirus4)) + " km/s.")