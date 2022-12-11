fail = open("kinganumbrid.txt", "r")
for kinganumber in fail:
    try:
        pikkus = 2 / 3 * (float(kinganumber) - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
