u = float(input("Sisesta esimene keha kiirus: "))
v = float(input("Siseta teise keha kiirus: "))
x = float(input("Siseta kolmanda keha kiirus: "))
y = float(input("Sisesta neljanda keha kiirus: "))

def summa(u,v):
    return (u+v)/(1+(u*v)/(c*c)) 

c = 299792.458

a = summa(u,v)
b = summa(a,x)
c = summa(b,y)

print("Kiiruste summa on", a, "km/s.")