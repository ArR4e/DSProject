def summa(u,v):
    return (u+v)/(1+(u*v/299792.458**2))

u = float(input("u "))
v = float(input("v "))
x = float(input("x "))
y = float(input("y "))

print(summa(summa(summa(u,v),x),y))