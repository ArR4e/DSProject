import math
def summa (u, v):
    c = (u+v)/(1+ (u*v/299792.458**2))
    return c
a = float(input("sisesta esimese keha kiirus: "))
b = float(input("sisesta teise keha kiirus: "))
x = (summa(a,b))
c = float(input("sisesta kolmanda keha kiirus: "))
x = summa(x,c)
d = float(input("sisesta neljanda keha kiirus: "))
print("kiiruste summa on ", summa(x,d))