c = 299792.458 #km/s
keha1 = float(input("Sisesta esimese keha kiirus vaatleja suhtes:"))
keha2 = float(input("Sisesta teise keha kiirus vaatleja suhtes:"))
keha3 = float(input("Sisesta kolmanda keha kiirus vaatleja suhtes:"))
keha4 = float(input("Sisesta neljanda keha kiirus vaatleja suhtes:"))

def summa(u,v):
    kiirused = (u + v)/(1 + (u*v)/c**2)
    return kiirused
print("Kiiruste summa on:", summa(summa(summa(keha1,keha2),keha3),keha4))