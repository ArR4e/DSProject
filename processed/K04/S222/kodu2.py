def summa(u,v):
    c = 299792.458   
    return (u+v)/(1+(u*v)/c**2)

u = float(input("Esimene kiirus: "))
v = float(input("Teine kiirus: "))
x = float(input("Kolmas kiirus: "))
y = float(input("Neljas kiirus: "))

print(summa(summa(u,v),summa(x,y)),"km/s")