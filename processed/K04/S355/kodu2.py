def summa (u,v):
    c = 299792.458
    return (u+v)/(1+(u*v/c**2))

u = float(input("Sisesta u väärtus: "))
v = float(input("Sisesta v väärtus: "))
x = float(input("Sisesta x väärtus: "))
y = float(input("Sisesta y väärtus: "))

print(summa(print(summa(print(summa(u,v))), x)), y)