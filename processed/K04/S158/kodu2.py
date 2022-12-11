c = 299792.458

def summa(u, v) :
    return (u + v) / (1 + ((u * v) / (c ** 2)))

u = int(input("Sisesta 1. keha kiirus: "))
v = int(input("Sisesta 2. keha kiirus: "))
s = int(input("Sisesta 3. keha kiirus: "))
t = int(input("Sisesta 4. keha kiirus: "))

kiirus_1 = summa(u, v)
kiirus_2 = summa(kiirus_1, s)
kiirus_3 = summa(kiirus_2, t)

print("Kiiruste summa on ", str(kiirus_3), " km/s")