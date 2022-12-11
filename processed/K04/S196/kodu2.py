def summa(u, v):
    return (u + v) / (1 + (u * v / 299792.458 ** 2))

u = float(input("Sisesta esimese keha kiirus: "))
v = float(input("Sisesta teise keha kiirus: "))
x = float(input("Sisesta kolmanda keha kiirus: "))
y = float(input("Sisesta neljanda keha kiirus: "))

print("Esimese keha kiirus vaatleja suhtes on:", u)
print("Teise keha kiirus vaatleja suhtes on:", summa(u, v))
print("Kolmanda keha kiirus vaatleja suhtes on:", summa(x, summa(u, v)))
print("Neljanda keha kiirus vaatleja suhtes on:", summa(y, (summa(x, summa(u, v)))))