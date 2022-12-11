import math

liin = int(input('Liini pikkus on: '))
kaugus = int(input('postide maksimaal kaugus on: '))

minim = math.ceil(liin/kaugus) + 1

print(minim)