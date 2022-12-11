def summa(a,b):
   return (a+b)/(1+((a*b)/299792.458**2))

s = float(input("1. keha kiirus vaatleja suhtes on: "))
for i in range(3):
    b = float(input(str(i+2)+". keha kiirus vaatleja suhtes on: "))
    s = summa(s,b)
    a = b
print("Kiiruste summa on",s,"km/s")