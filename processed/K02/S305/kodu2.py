import math

pikkus = int(input("Sisesta liini pikkus: "))
kaugus = int(input("Sisesta postide maksimaalkaugus: "))
post = pikkus / kaugus + 1

print(math.ceil(post))