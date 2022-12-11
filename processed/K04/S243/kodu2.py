#Einsteini erirelatiivsusteooria

def summa(u, v):
    c=299792.458 #km/s
    return (u+v)/(1+(u*v)/c**2)

e=float(input("Esimese keha kiirus vaatleja suhtes on: "))
t=float(input("Teise keha kiirus esimese keha suhtes on: "))
k=float(input("Kolmanda keha kiirus teise keha suhtes on: "))
n=float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
sum1=summa(e, t)
print(sum1)
sum2=summa(sum1, k)
print(sum2)
sum3=summa(sum2, n)
print(sum3)
print("Kiiruste summa on", sum3,  "km/s.")