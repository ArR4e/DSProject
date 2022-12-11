def summa(u,v):
    return (u+v)/(1+((u*v)/(c**2)))

c = 299792.458
u = float(input("Palun sisestage kiiruse u väärtus (km/s): "))
v = float(input("Palun sisestage kiiruse v väärtus (km/s): "))
x = float(input("Palun sisestage kiiruse x väärtus (km/s): "))
y = float(input("Palun sisestage kiiruse y väärtus (km/s): "))

print('Kiiruste summa on', summa(summa(summa(u,v),x),y) , 'km/s')