fail = open('kinganumbrid.txt')

for rida in fail:
    try:
        kinganumber = float(rida.strip())
        rida = 2/3 * (kinganumber - 2)
        print(round(rida))
    except:
        print("Vigane sisend")

fail.close()