f = open('kinganumbrid.txt', encoding='UTF-8')

for rida in f:
    try:
        kinganumber = rida.strip()
        pikkus = round(2/3 * (float(kinganumber) - 2))
        print(pikkus)
    except:
        print("Vigane sisend")

f.close()

    