f = open("kinganumbrid.txt")

for rida in f:
    try:
        kinganumber = float(rida)
        pikkus = 2/3 * (kinganumber - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")