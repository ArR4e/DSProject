
c = 299792.458
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Esimese keha kiirus vaatleja suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input(" Neljanda keha kiirus kolmanda keha suhtes on: "))



def summa(u,v):
    return (u+v)/(1+u*v/c**2)
print("Kiiruste summa on" , summa(summa(u,v),summa(kolmas,neljas)) , "km/s")