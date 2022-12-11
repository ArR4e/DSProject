c=299792.458
a = float(input("Ütle esimese kiirus. "))
b = float(input("Ütle teise kiirus. "))
d = float(input("Ütle kolmanda kiirus. "))
e = float(input("Ütle neljanda kiirus. "))

def summa(u, v):
    kiirus = (u + v)/(1+(u*v)/(c*c))
    return kiirus

kiirusvalgus = summa(summa(summa(a,b),d),e)

print("Kiiruste summa on", kiirusvalgus)