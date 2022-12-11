def summa(u, v):
    u = float(u)
    v = float(v)
    c = 299792.458 #299792,458
    return (u + v)/(1 + (u*v)/c**2)

a = input("Kiirus 1: ")
b = input("Kiirus 2: ")
c = input("Kiirus 3: ")
d = input("Kiirus 4: ")



print(summa(summa(a, b), summa(c, d)))