

def summa(u, v):
    ens = (u + v) / (1 + (u * v) / c ** 2)
    return ens
c = 299792458
u1 = float(input("Sisestage palun esimesekeha kiirust: "))
v1 = float(input("Sisestage palun teisekeha kiirust: "))
x1 = float(input("sisestage palun kolmandakeha kiirust: "))
z1 = float(input("Sisetage palun neljandakeha kiirust: "))

m1 = summa(u1, v1) #2keha vaatleja suunda
print(m1)
m2 = summa(v1, x1)
print(m2)
m3 = summa(x1, z1)
print(m3)