u = float(input("Esimese keha kiirus vaatleja suhtes: "))
v = float(input("Teise keha kiirus esimese keha suhtes: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes: ")) 
y = float(input("Neljanda keha kiirus kolmanda suhtes: "))
c = 299792.458
def summa(u, v):
    
    return (u + v)/(1 + (u*v / (c**2)))
summa1 = summa(u, v)
summa2 = summa(summa1, x)
summa3 = summa(summa2, y)

print("Summa on", summa3, "km/s")


