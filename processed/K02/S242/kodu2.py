import math
a = input("Sisesta elektriliini pikkus täisarvuna meetrites ")
b = input("Sisesta maksimaalne kõrvutiasetsevate postide kaugus täisarvuna meetrites ")
a = int(a)
b = int(b)
c = a / b + 1
c = int(math.ceil(c))
print("Minimaalne postide arv on", c)