c=299792.458  # valguse kiirus km/s
u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus vaatleja suhtes on: "))
x=float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y=float(input("Neljanda keha kiirus vaatleja suhtes on: "))
def summa(u, v):
    uv_summa=(u+v)/(1+(u*v)/(c**2))
    return uv_summa
summa1=summa(u, v)
summa2=summa(summa1, x)
lõppsumma=summa(summa2, y)
print("Kiiruste summa on " + str(lõppsumma) + " km/s.")