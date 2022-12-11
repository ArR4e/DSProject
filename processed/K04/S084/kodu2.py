def summa(a, b):
    tulemus = (a + b) / (1 + (a*b) / 299792.458 ** 2)
    return tulemus

while True:
    try:
        u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
        v = float(input("Teise keha kiirus esimese keha suhtes on: "))
        x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
        y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
        break
    except:
        print("Midagi valesti")

print(f"Kiiruste summa on {summa(summa(summa(u, v), x), y)} km/s")