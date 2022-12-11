f = open("kinganumbrid.txt", encoding="UTF-8")

for rida in f:
    try:
        rida_ = float(rida.strip())
        pikkus = 2 / 3 * (rida_ - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
        





#pikkus = 2/3 * (kinganumber - 2)



f.close()