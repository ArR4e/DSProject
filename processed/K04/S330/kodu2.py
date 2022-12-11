c = 299792.458

u = float(input("Esimese keha kiirus (m/s): "))
v = float(input("Teise keha kiirus (m/s): "))
x = float(input("Kolmanda keha kiirus (m/s): "))
y = float(input("Neljanda keha kiirus (m/s): "))

def summa(u, v):
    return (u + v)/(1 + u * v/c ** 2)

print("Esimese keha kiirus vaatleja suhtes on", u, "m/s.")
print("Teise keha kiirus esimese keha suhtes on", summa(v, x), "m/s.")
print("Kolmanda keha kiirus teise keha suhtes on", summa(v, x), "m/s.")
print("Neljanda keha kiirus kolmanda keha suhtes on", summa(x, y), "m/s.")
print("Kiiruste summa on", u + v + x + y, "m/s.")