f = open("kinganumbrid.txt")

for rida in f:

    try:
        kinganr = float(rida.strip())
        pikkus = round(2/3 * (kinganr - 2))
        print(pikkus)
    except:
        print("Vigane sisend")

