a = int(input("Sisesta liini pikkus täisarvuna meetrites:"))
b = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites:"))

from math import *
x = ceil(a / b)


print("Liini ehitamiseks on minimaalselt tarvis " + str(x + 1) + " posti.")