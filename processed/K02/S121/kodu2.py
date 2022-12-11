import math

liin = int(input("Sisesta liini pikkust: "))
kaugus = int(input("Sisesta maksimaalkaugust: "))
if liin<kaugus:
    print(2)
else:
    print(math.ceil(liin/kaugus)+1)
