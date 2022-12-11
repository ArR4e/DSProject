import math
pikkus = int(input("Sisesta kui pikk on liin: "))
kaugus = int(input("Sisesta maksimaalne postide vaheline kaugus"))
poste = pikkus/kaugus+1
print(int(math.ceil(poste)))