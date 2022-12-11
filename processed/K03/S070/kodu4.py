import math

f = open("kinganumbrid.txt", "r", encoding='UTF-8')
for rida in f:
    try:
        print(round((float(rida) - 2) * 2 / 3))
    except:
        print("Vigane sisend")
f.close()

