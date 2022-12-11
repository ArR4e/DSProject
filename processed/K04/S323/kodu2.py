def summa(u, v):
    c = 299792.458
    a = u + v
    b = u * v
    jagamine = b/(c**2)
    
    valem = a/(1+jagamine)
    
    return valem


u = float(input("Sisestage 1. keha kiirus: "))
v = float(input("Sisestage 2. keha kiirus: "))
x = float(input("Sisestage 3. keha kiirus: "))
y = float(input("Sisestage 4. keha kiirus: "))

keha1 = summa(u, v)
keha2 = summa(x, keha1)
keha3 = summa(y, keha2)

print("Kiiruste summa on: ", keha3, " km/s.")