u=float(input("Esimene keha liigub vaatleja suhtes kiirusega: (km/s) "))
v=float(input("Teine keha liigub esimese suhtes kiirusega: (km/s) "))
x=float(input("Kolmas keha liigub teise suhtes kiirusega: (km/s) "))
y=float(input("Neljas keha liigub kolmanda suhtes kiirusega: (km/s) "))
c=float(299792.458)

def summa(u,v):
    return (u+v)/(1+((u*v)/c**2))
print("Kõikide summa on",summa(summa(summa(u,v),x),y),"km/s")