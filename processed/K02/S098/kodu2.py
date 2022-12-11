import math

a = int(input("Sisesta liini pikkus: "))
b = int(input("Sisesta pastide vahekaugus: "))

c = math.ceil(a/b)

print("Minimaalne postide arv on" +" "+str( c+1))
