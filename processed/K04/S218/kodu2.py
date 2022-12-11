
def summa (u, v):
    c= 299792.458
    summa = ((u+v) / (1+((u*v) / (c*c))))
    return summa
    
a = float(input("Sisesta esimene kiirus: "))
b = float(input("Sisesta teine kiirus: "))
d = float(input("Sisesta kolmas kiirus: "))
v = float(input("Sisesta neljas kiirus: "))

c= 299792.458
kokkuab = ((a+b) / (1+((a*b) / (c*c))))
u = ((kokkuab+d) / (1+((kokkuab*d) / (c*c))))


print(summa(u, v), "km/s")