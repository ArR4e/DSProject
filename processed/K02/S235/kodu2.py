import math
a = input("Sisestage elektriliini pikkus (täisarvuna meetrites): ")
b = input("Sisestage kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): ")
c=int(a)/int(b)
d = math.ceil(c)
print(d+1)