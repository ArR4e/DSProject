u = float(input("Esimene keha vaatle suhtes: "))
v = float(input("Teine keha esimese suhtes:"))
x = float(input("Kolmas keha teise suhtes:"))
y = float(input("Neljas keha kolmanda suhtes:"))
arvude_summa = u + v + x + y
korrutis = u * v * x * y
valem = (arvude_summa) / (1 + ((korrutis) / 299792.458**2))
def summa(u,v,x,y):
    valem
    return valem

print("Kiiruste summa on", summa(u , v, x, y), "km/s")