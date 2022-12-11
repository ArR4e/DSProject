import math

a = int(input("Sisesta liini pikkus: "))
b = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus: "))

x = math.ceil(a / b) + 1

print(x)

