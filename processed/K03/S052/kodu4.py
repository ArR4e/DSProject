f = open("kinganumbrid.txt")

for rida in f:
    try:
        kinganr = float(rida)
        pikkus = 2 / 3 * (kinganr - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
    