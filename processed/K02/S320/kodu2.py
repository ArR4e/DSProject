from math import ceil

a=int(input("Sisesta liini pikkus täisarvuna meetrites:"))
b=int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus täisarvuna meetrites:"))
print(ceil(a/b+1))