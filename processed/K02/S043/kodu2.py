import math

a=int(input("Liini pikkus: "))
b=int(input("Kõrvutiasetsevade postide maksimaalkaugus: "))
c=math.ceil(a/b+1)
print(c)