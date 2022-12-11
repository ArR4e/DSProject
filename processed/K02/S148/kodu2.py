import math
from math import ceil

a = int(input("Sisesta liini pikkus: "))
b = int(input("Sisesta kahe kõrvutiasetsevate postide kaugus: "))

c = (a / b + 1)

print(math.ceil(c))