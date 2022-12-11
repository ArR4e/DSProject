
fail = open('kinganumbrid.txt')
rida = fail.readline()
while rida != "":
    try:
        pikkus = 2/3 * (float(rida) - 2)
        rida= fail.readline()
        print(round(pikkus))
    except:
        print("Vigane seisund")
        rida= fail.readline()
    
fail.closed



