from math import *

liin = int(input("Sisesta liini pikkus: "))
vahe = int(input("Sisesta maksimaalne postide vahe: "))

post = ceil(liin/vahe)+1

print(post)