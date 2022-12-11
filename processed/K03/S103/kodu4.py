fail = open("kinganumbrid.txt", encoding="UTF-8")

for rida in fail:
    try:
        nr = float(rida)
        pikkus = round(2/3 * (float(nr) - 2))
        print(pikkus)
    except:
        print("Vigane sisend")