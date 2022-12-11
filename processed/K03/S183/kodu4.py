fail = open("kinganumbrid.txt", encoding="UTF- 8")
f = fail.readlines()

for rida in f:
    try:
        king = float(rida)
        pikkus = 2/3 * (king - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")

fail.close()