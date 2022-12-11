def summa(u, v):
    kiirus=((u+v)/(1+(u*v/299792.458^2)))
    return summa
    
u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus esimese keha suhtes on: "))
x=float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y=float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

summa1=summa(u, v)
summa2=summa(summa1, x)
summa3= summa(summa2, y)

print("Kiiruste summa on ", summa3, " km/s.")