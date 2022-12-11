f = open("kinganumbrid.txt")

while True:
    rida = f.readline()
    if rida == "":
        break
    if rida.strip().replace(".", "").isdigit() == True and rida.strip().count('.') < 2:
        kinganumber = float(rida.strip())
        pikkus = 2/3*(kinganumber-2)
        print(round(pikkus))
    else:
        print("Vigane sisend")
f.close()