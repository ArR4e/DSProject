c = 299792.458

def summa(u,v):
    kiirustesumma = float((u+v)/(1+u*v/c**2))
    return kiirustesumma

u = float(input("Esimese keha kiirus: "))
v = float(input("Teise keha kiirus: "))
x = float(input("Kolmanda keha kiirus: "))
y = float(input("Neljanda keha kiirus: "))
uv = summa(u,v)
uvx = summa(uv,x)
uvxy = summa(uvx,y)


print("Kiiruste summa on " + str(uvxy) + " km/h")




