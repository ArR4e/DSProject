def summa(u, v):
    c = 299792.458
    tulemus = (u+v)/(1+(u*v)/c**2)
    return tulemus
u = float(input("Sisestage esimese keha kiirus: "))
v = float(input("Sisestage teise keha kiirus: "))
x = float(input("Sisestage kolmanda keha kiirus: "))
y = float(input("Sisestage neljanda keha kiirus: "))
tulemus = summa(u,v)
tulemus = summa(tulemus,x)
print("Kiiruste summa on", summa(tulemus,y), "km/s.")