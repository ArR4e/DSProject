import math
liin= int(input("Kui pikk on liin? "))
vahe= int(input("Kui pikk on maksimaalne postide vahe? "))
post=float(liin/vahe)
print(math.ceil(post) + 1)