def summa(u, v):
    c = 299792.458
    return (u+v) / (1 + ((u*v) / (c**2)))

u = input("Sisestage esimene kiirus: ")
v = input("Sisestage teine kiirus: ")
x = input("Sisestage kolmas kiirus: ")
y = input("Sisestage neljas kiirus: ")

u_v = summa(float(u), float(v))
u_v_x = summa(float(u_v), float(x))
u_v_x_y = summa(float(u_v_x), float(y))
print("Kiiruste summa on: " + str(u_v_x_y))