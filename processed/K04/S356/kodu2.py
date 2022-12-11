c = float(299792.458)

u = abs(float(input("Sisesta esimese keha kiirus vaatleja suhtes: ")))
v = abs(float(input("Sisesta teise keha kiirus esimese keha suhtes: ")))
x = abs(float(input("Sisesta kolmanda keha kiirus teise keha suhtes: ")))
y = abs(float(input("Sisesta neljanda keha kiirus kolmanda keha suhtes: ")))

def summa(u,v):
    sum1 = ((u + v) / (1 + ((u * v) / (c**2) )))
    sum2 = ((sum1 + x) / (1 + ((sum1 * x) / (c**2) )))
    return((sum2 + y) / (1 + ((sum2 * y) / (c**2) )))
    
summa(u,v)
print("Kiiruste summa on " + str(summa(u,v)) + " km/s.")