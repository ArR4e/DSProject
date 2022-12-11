import math

f = open("kinganumbrid.txt")

rida = 0
for line in f:
    if line != "\n":
        rida += 1
f.close()

f = open("kinganumbrid.txt")

i = 0
while i < rida:
    try:
        arv = f.readline()
        pikkus = (2 / 3) * (int(float(arv)) - 2)
        print(round(pikkus))
        i += 1
    except:
        print("Vigane sisend")
        i += 1
f.close()