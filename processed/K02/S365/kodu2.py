from math import *

liin = float(input("Kui pikk on liin? : "))
maksimum = float(input("Mis on postide vaheline maksimaalne kaugus? "))

postide_arv = ceil(maksimum)


x=((liin / postide_arv))
print (ceil(x))
