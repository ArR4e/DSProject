import math

x = input("Sisesta elektriliini pikkus meetrites: ")
a=int(x)

y = input("Sisesta postidevaheline kaugus meetrites: ")
b=int(y)

z = ((a/b) + 1)

vastus=math.ceil(z)

print("Poste on vaja: " , str(vastus))




