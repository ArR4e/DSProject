def summa(u,v):
    summa1 = (u + v)/(1+((u*v)/299792458**2))
    u = summa1
    v = x
    summa2 = (u + v)/(1+((u*v)/299792458**2))
    u = summa2
    v = y
    summa3 = (u + v)/(1+((u*v)/299792458**2))
    return summa3
u = float(input("Sisesta esimese keha kiirus vaatleja suhtes:"))
v = float(input("Sisesta teise keha kiirus esimese keha suhtes:"))
x = float(input("Sisesta kolmanda keha kiirus teise keha suhtes:"))
y = float(input("Sisesta neljanda keha kiirus kolmanda keha suhtes:"))
print ("Kiiruste summa on", summa(u,v))
