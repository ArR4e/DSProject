f = open("kinganumbrid.txt")
while True:
    rida = f.readline()
    if rida == "":
        break
    try:
        kinganumber = float(rida)
        pikkus = round(2/3*(kinganumber-2))
        print(pikkus)
    except:
        print("Vigane sisend")