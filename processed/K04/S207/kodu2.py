def summa(u, v):
    return (u+v)/(1+(u*v)/(299792.458)**2)

u = float(input("Sisestage esimese keha kiirus vaatleja suhtes: "))
v = float(input("Sisestage teise keha kiirus esimese keha suhtes: "))
u = summa(u,v)
v = float(input("Sisestage teise keha kiirus kolmanda keha suhtes: "))
u = summa(u,v)
v = float(input("Sisestage kolmanda keha kiirus neljanda keha suhtes: "))

print(f"Kiiruste summa on {summa(u,v)} km/s")