f = open("kinganumbrid.txt")
for z in f.readlines():
    try:
        print(round(2 / 3 * (float(z) - 2)))
    except:
        print("Vigane sisend")
f.close()