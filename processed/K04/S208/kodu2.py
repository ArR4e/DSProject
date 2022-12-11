u = float(input("u = "))
v = float(input("v = "))
x = float(input("x = "))
y = float(input("y = "))
c = 299792.458
def summa(u, v):
    return (u + v) / (1 + (u * v) / c ** 2)
def summa(x, y):
    return (x + y) / (1 + (x * y) / c ** 2)
y = summa(x, y)
x = summa(u, v)
def summa(x, y):
    return (x + y) / (1 + (x * y) / c ** 2)
print("Kiiruste summa on", summa(x, y), "km/s")