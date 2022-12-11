c=299792.458
a=True
def summa(kiirus1,kiirus2, kiirus3):
        kiirusa=(kiirus1+kiirus2)/(1+((kiirus1*kiirus2)/c**2))
        kiirus1=kiirusa
        if kiirus3=="":
            a==False
            return kiirusa
summa(kiirus1=float(input("Esimese keha kiirus vaatleja suhtes on: ")),
kiirus2=float(input("Teise keha kiirus esimese keha suhtes on: ")),
kiirus3=str(input()))
while a==True:
    summa(kiirus1=float(input("Esimese keha kiirus vaatleja suhtes on: ")),
    kiirus2=float(input("Teise keha kiirus esimese keha suhtes on: ")),
    kiirus3=str(input()))