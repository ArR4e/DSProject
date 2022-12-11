#2. Einsteini erirelatiivsusteooria
u = float(input("Sisesta esimese keha kiirus vaatleja suhtes: "))
v = float(input("Sisesta teise keha kiirus esimese keha suhtes: "))
x = float(input("Sisesta kolmanda keha kiirus teise keha suhtes: "))
y = float(input("Sisesta neljanda keha kiirus kolmanda keha suhtes: "))

def summa(u, v, x, y):
    return ((u + v) / (1 + u * v / (299792.458 ** 2))) + ((v + x) / (1 + v * x / (299792.458 ** 2))) + ((x + y) / (1 + x * y / (299792.458 ** 2)))

print("Kiiruste summa on: ")
print(summa(u, v, x, y))