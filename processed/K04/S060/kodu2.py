e = float(input("Esimese keha kiirus vaatleja suhtes on:"))
t = float(input("Teise keha kiirus esimese keha suhtes on:"))
k= float(input("Kolmanda keha kiirus teise keha suhtes on:"))
n= float(input("Neljanda keha kiirus kolmanda keha suhtes on:"))
c=299792.458
def summa (u,v):
    vastus=(u+v)/(1+u*v/(c*c))
    return vastus
print("Kiiruste summa on "+str(summa(summa(summa(e,t),k),n))+" km/s")