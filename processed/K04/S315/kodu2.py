def summa(u, v):
    c = 299792.458 #m/s
    return (u+v)/(1+((u*v)/c**2))

u = float(input("Kiirus1 "))
v = float(input("Kiirus2 "))
x = float(input("Kiirus3 "))
y = float(input("Kiirus4 "))

summa1 = summa(u,v)
summa2 = summa(summa1, x)
summa3 = summa(summa2, y)

print("Kiiruste summa on " + str(summa3) + " km/h")