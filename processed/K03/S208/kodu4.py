f = open("kinganumbrid.txt")
while True:
    rida = f.readline()
    if rida == "":
        break
    try:
        number = float(rida.strip())
        pikkus = 2 / 3 * (number - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
f.close()