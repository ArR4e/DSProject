f = open("kinganumbrid.txt")
while True:
    rida = f.readline()
    if rida == "":
        break
    else:
        try:
            kinganumber = float(rida)
            pikkus = 2/3 * (kinganumber - 2)
            print(round(pikkus))
        except:
            print("Vigane sisend")