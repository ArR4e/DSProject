fail = open('kinganumbrid.txt')

for rida in fail:
    try:
        kinganumber = float(rida.strip())
        pikkus = 2 / 3 * (kinganumber - 2)
        ü_arv = round(pikkus)
        print(ü_arv)
    except:
        print('Vigane sisend')