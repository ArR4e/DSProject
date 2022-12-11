def summa(u,v):
    c = 299792.458
    kiirus = (u + v) / (1 + (u * v / c**2))
    return kiirus


u = float(input("Palun sisesta esimese keha kiirust: "))
v = float(input("Palun sisesta teise keha kiirust: "))
x = float(input("Palun sisesta kolmanda keha kiirust: "))
y = float(input("Palun sisesta neljanda keha kiirust: "))

uvkiirus = summa(u,v)
uvxkiirus = summa(uvkiirus, x)
uvxykiirus = summa(uvxkiirus, y)
print("Kiiruste summa on ", str(uvxykiirus), "km/s")



