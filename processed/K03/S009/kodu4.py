f = open('kinganumbrid.txt')

while True:
    try:
        rida = f.readline()
        number = float(rida.strip())
        pikkus = 2/3*(number-2)
        pikkus_ymar = round(pikkus, 1)
        print("Jalalaba pikkus on ", str(pikkus_ymar), " cm.")
    except:
        print("Vigane sisend")
    if rida == "":
        break

f.close()