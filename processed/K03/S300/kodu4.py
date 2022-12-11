fail = open("kinganumbrid.txt")
for rida in fail:
    try:
        king = float(rida.strip())
        pikkus = round(2 / 3 * (king - 2))
        print(pikkus)
    except:
        print("Vigane sisend")