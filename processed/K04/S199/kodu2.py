

def summa(u, v):
    c = 299792.458
    
    summa_u_v = (u + v) / (1 + u*v/c**2)
    summa_uv_x = (summa_u_v + x) / (1 + summa_u_v*x/c**2)
    relatiivsus = (summa_uv_x + y) / (1 + summa_uv_x*y/c**2)
    print("Kiiruste summa on: ", relatiivsus, "km/s.")
   
u = float(input("Kirjuta esimese keha kiirus: "))
v = float(input("Kirjuta teise keha kiirus: "))
x = float(input("Kirjuta kolmanda keha kiirus: "))
y = float(input("Kirjuta neljanda keha kiirus: "))

summa(u, v)
