f = open("kinganumbrid.txt")

while True:
    rida = f.readline()
    if rida == "":
        break
    try:
        kinganumber = float(rida.strip())
        pikkus = 2/3 * (kinganumber-2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
f.close()