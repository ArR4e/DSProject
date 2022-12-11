def summa(a, b):
    c = 299792.458
    return (a + b) / (1 + (a * b /c**2))
    
u = float(input("Sisesta esimese keha kiirus: "))
v = float(input("Sisesta teise keha kiirus: "))
x = float(input("Sisesta kolmanda keha kiirus: "))
y = float(input("Sisesta neljanda keha kiirus: "))

magic = summa(summa(u, v), summa(x, y))

print(magic)