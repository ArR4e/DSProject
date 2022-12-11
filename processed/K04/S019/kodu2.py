u = float(input("Esimese keha kiirus vaatleja suhtes: "))
v = float(input("Teise keha kiirus vaatleja suhtes: "))
x = float(input("Kolmanda keha kiirus vaatleja suhtes: "))
y = float(input("Neljanda keha kiirus vaatleja suhtes: "))
c = 299792.458

esimene = (u + v) / (1 + ( u*v)/ c**2)
teine = (esimene + x) / (1 + ( esimene*x)/ c**2)

def summa( u, v, x, y,esimene, teine, c = 299792.458):
    
    return((teine + y) / (1 + ( teine * y)/ c**2))
    
print("Kiiruste summa on",summa(u,v,x,y, esimene, teine, c = 299792.458), "km/h")