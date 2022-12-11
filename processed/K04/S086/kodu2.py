#Relatiivsusteooria

def summa(u, v):
    return (u+v)/(1+(u*v)/299792.458**2)

kiirus1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
kiirus2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
kiirus3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
kiirus4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

print("Kiiruste summa on ", summa(summa(summa(kiirus1, kiirus2), kiirus3), kiirus4), " km/s")