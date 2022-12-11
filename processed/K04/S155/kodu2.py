c = 299792.458
u = float(input("esimese keha kiirus: "))
v = float(input("teise keha kiirus: "))
x = float(input("kolmanda keha kiirus: "))
y = float(input("neljanda keha kiirus: "))

def summa(u, v, x, y):
    kiiruskahe = (u + v) / (1+(u*v/c**2))
    return kiiruskahe
    kiiruskolme = (kiiruskahe + x) / (1+(kiiruskahe*x/c**2))
    return kiiruskolme
    kiirusnelja = (kiiruskolme + x) / (1+(kiiruskolme*y/c**2))
    
print("Kiiruste summa on {} km/s." .format(summa(u, v, x, y)))
