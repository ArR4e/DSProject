u = float(input("Esimene keha kiirus: "))
v = float(input("Teise keha kiirus: "))
x = float(input("Kolmanda keha kiirus: "))
y = float(input("Neljanda keha kiirus: "))
c = 299792.458
def summa(u,v):
    a = ((u+v)/(1+(u*v/c**2)))
    return a
print(summa(summa(summa(u,v), x), y))