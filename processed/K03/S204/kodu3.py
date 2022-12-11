import math

n = int(input("Palun sisesta naturaalarv n: "))
a = int((n+(n+1)+(n+2)+(n+3)+(n+4)+(n+5)+(n+6)+(n+7)+(n+8)+(n+9))**2)
b = int(n**2+(n+1)**2+(n+2)**2+(n+3)**2+(n+4)**2+(n+5)**2+(n+6)**2+(n+7)**2+(n+8)**2+(n+9)**2)
if n >= 0:
     print(a-b)
else:
    print("Arv pole naturaalarv, palun sisesta naturaalarv")