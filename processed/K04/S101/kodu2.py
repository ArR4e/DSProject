c=299792.458
u=float(input("sisesta esimese keha kiirus vaatleja suhtes:"))
v=float(input("sisesta teise keha kiirus esimese keha suhtes:"))
x=float(input("sisesta kolmanda keha kiirus teise keha suhtes:"))
y=float(input("sisesta neljanda keha kiirus kolmanda keha suhtes:"))
def summa(a,b):
    return((a+b)/(1+((a*b)/(c**2))))
print("Kiiruste summa on", summa(summa(summa(u,v),x),y),"kilomeetrit sekundis.")