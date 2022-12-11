a = float(input("Sisesta esimese keha kiirus: "))
b = float(input("Sisesta teise keha kiirus: "))
x = float(input("Sisesta kolmanda keha kiirus: "))
y = float(input("Sisesta neljanda keha jiirus: "))
c = 299792.458

def summa(u, v):
    return (u + v) / ((1 + ((u * v) / (c ** 2))))

kiiruse_summa = (summa(summa(summa(a, b), x), y))
print("Kiiruste summa on: ", kiiruse_summa)