from math import ceil
x = int(input("Sisesta liini pikkus (täisarvuna meetrites): "))
y = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))
z = x / y + 1

print("Minimaalselt on liini ehitamiseks vaja", ceil(z) , "posti")