def summa(u,v):
    return (u+v)/(1+u*v/(c**2))

u = float(input("Esimese keha kiirus vaatleja suhtes (km/s): "))
v = float(input("Teise keha kiirus vaatleja suhtes(km/s): "))
x = float(input("Kolmanda keha kiirus vaatleja suhtes(km/s): "))
y = float(input("Neljanda keha kiirus vaatleja suhtes(km/s): "))
c = float(299792.458)
z = (summa(u,v))
u = z
v = x
g = (summa(u,v))
u = g
v = y
t = (summa(u, v))
print("Kiiruste summa on ",t , "km/h")
