from math import *
a = int(input("Sisestage liini pikkus: "))
b = int(input("Sisestage postide vaheline maksimaalkaugus: "))
c = a / b
d = ceil(c)
print("Minimaalne vajaminevate postide hulk on:", d)