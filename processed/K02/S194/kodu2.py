from math import ceil

lp = int(input("Liini pikkus (täisarvuna meetrites): "))
mk = int(input("Kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))

pa = 1
a = 0
while a < lp:
    a += mk

print("Poste läheb vaja: " + str(pa + ceil(a/mk)))