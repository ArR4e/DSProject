f = open("kinganumbrid.txt")
for rida in f:
    try:
        kinganr = float(rida.strip())
        pikkus = 2 / 3 * (round(kinganr) - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
