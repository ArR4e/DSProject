from math import *
distance = int(input("Mis on liini pikkus?\n"))
max_distance = int(input("Mis on postidevaheline maksimaalkaugus?\n"))
poles = ceil(distance/max_distance) + 1
print(poles)