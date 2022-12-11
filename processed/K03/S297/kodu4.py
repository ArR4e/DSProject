from math import *

f = open("kinganumbrid.txt")

for x in f :
    try:
        kinganr = float(x)
        pikkus = round((2/3) * (kinganr - 2))
        print(pikkus)
    
    except:
        print('Vigane sisend')
f.close